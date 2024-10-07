from django.shortcuts import render
from rest_framework import generics, views
from rest_framework.response import Response
from rest_framework import status
from .models import JobProfile
from .serializers import JobsSerializers


class JobListCreateApiView(generics.ListCreateAPIView):
    queryset  = JobProfile.objects.all()
    serializer_class = JobsSerializers

class JobRecommendListApiView(generics.ListCreateAPIView):
    queryset  = JobProfile.objects.all()
    serializer_class = JobsSerializers

    def get_skills_based(self, user_skills):
        matching_jobs = []
        for job in JobProfile.objects.all():
                required_skills = job.required_skills
                if any(skill in required_skills for skill in user_skills):
                    matching_jobs.append(job)

        job_id = [i.pk for i in matching_jobs]
        req_skills_match = JobProfile.objects.filter(pk__in=job_id)
        return req_skills_match
        

    def get(self, request, *args, **kwargs):
        return Response({"Message": "Get request is not defined here."})
    
    def post(self, request, *args, **kwargs):
        user_data=request.data

        if not all(field in user_data for field in ["skills", "experience_level", "preferences"]):
            return Response({"field Error": "Enter all required fields"}, status=400)
    
        user_skills = user_data["skills"]
        user_exp_level = user_data["experience_level"]
        user_desired_roles = user_data["preferences"]["desired_roles"]
        user_locations = user_data["preferences"]["locations"]
        user_job_type = user_data["preferences"]["job_type"]

        exp_level_match = JobProfile.objects.all().filter(experience_level=user_exp_level)
        job_type_match = JobProfile.objects.all().filter(job_type=user_job_type)
        location_match = JobProfile.objects.all().filter(location__in=user_locations)
        job_title_match = JobProfile.objects.all().filter(job_title__in=user_desired_roles)
        req_skills_match = self.get_skills_based(user_skills)

        combined_queryset = exp_level_match.intersection(job_type_match, location_match, job_title_match, req_skills_match)

        serializer = self.get_serializer(combined_queryset, many=True)

        return Response(serializer.data)
    