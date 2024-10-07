from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import UserProfile
from .serializers import UsersSerializers
from jobs.models import JobProfile
from jobs.serializers import JobsSerializers

class UserListCreateApiView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UsersSerializers

class JobRecommendBasedUserListApiView(generics.ListAPIView):
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
        print(kwargs)
        id = kwargs['pk']
        print(id)
        user_list = list(UserProfile.objects.filter(id=id).values())

        if not user_list:
            return Response({"Not Exist":"They user id is not present"})     
        
        user_data = user_list[0]
        if not all(field in user_data for field in ["skills", "experience_level", "preferences"]):
            return Response({"field Error": "Enter all required fields"}, status=400)
    
        user_skills = user_data["skills"]
        user_exp_level = user_data["experience_level"]
        user_desired_roles = user_data["preferences"]["desired_roles"]
        user_locations = user_data["preferences"]["locations"]
        user_job_type = user_data["preferences"]["job_type"]

        exp_level_match = JobProfile.objects.filter(experience_level=user_exp_level)
        job_type_match = JobProfile.objects.filter(job_type=user_job_type)
        location_match = JobProfile.objects.filter(location__in=user_locations)
        job_title_match = JobProfile.objects.filter(job_title__in=user_desired_roles)
        req_skills_match = self.get_skills_based(user_skills)

        combined_queryset = exp_level_match.intersection(job_type_match, location_match, job_title_match, req_skills_match)

        serializer = self.get_serializer(combined_queryset, many=True)

        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        return Response({"Message": "Post request is not defined here."})
    