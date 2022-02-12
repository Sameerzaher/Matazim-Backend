from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication 
from django.contrib.auth.models import User 
from .serializers import UserSerializer, CourseSerializer, LessonSerializer, UserCoursesSerializer, UserLessonsSerializer, UserProfileSerializer, ClassSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Course, Lesson, UserCourses, UserLessons, UserProfile, Class
from rest_framework import status
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer 
    permission_classes = (AllowAny,)

    @action (detail=True, methods = ['POST'])
    def getuser(self, request, pk=None):
        user = User.object.get(id=pk)
    
    # @action (detail=True, methods = ['POST'])
    # def getUserDetails(self, request, pk=None):
    #         print("im here in get user details")
    #         user = request.user
    #         print("user from query is: ", user)
    #         arr=[]
    #         u = User.objects.get(username='yarinAAA')
    #         print("user mail is: ", u.email)
    #         print("user name is: ", u.name)
    #         print("user surname is: ", u.lastName)
    #         userDetails= User.objects.filter(user=user.id, course=pk)
    #         for userCourse in userCourses:
    #             serializers = UserCoursesSerializer(userCourse, many=False)
    #             arr.append(serializers.data)
                
    #         response = {'message': 'Get', 'results': arr }
    #         return Response (response, status=status.HTTP_200_OK)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer 
    authentication_classes = (TokenAuthentication, )

    @action (detail=True, methods = ['POST'])
    def createUserProfile(self, request, pk=None):
        print("inside create user profile")
        username = request.data['username']
     
        getUser= User.objects.filter(username=username)       
                          
        newUser = UserProfile.objects.create(user=getUser[0], username=username, firstName=' ',lastName=' ',aboutMe= ' ', hobbies = ' ', badges=0, myGoal= '' )
        newUser.save()
        print("user is: ", newUser)
           
        response = {'message': 'created', 'results': newUser }
        return Response (response, status=status.HTTP_200_OK)


    @action (detail=True, methods = ['POST'])
    def getUserByUsername(self, request, pk=None):
            username = request.data['username']
            arr=[]
            u = UserProfile.objects.get(username=username)
           
            serializers = UserProfileSerializer(u, many=False)
            
                
            response = {'message': 'Get', 'results': serializers.data }
            print("response:", response)
            return Response (response, status=status.HTTP_200_OK)

    @action (detail=True, methods = ['POST'])
    def getUserDetails(self, request, pk=None):
            print("im here")
            user = request.user
            print("user from query is: ", user)
            arr=[]
            u = UserProfile.objects.get(user=user)
            # print("user mail is: ", u.email)
            print("user name is: ", u.firstName)
            print("user surname is: ", u.lastName)
            # userDetails= User.objects.filter(user=user.id, course=pk)
            # for userCourse in userCourses:
            u.username=user
            serializers = UserProfileSerializer(u, many=False)
            #     arr.append(serializers.data)
                
            response = {'message': 'Get', 'results': serializers.data }
            return Response (response, status=status.HTTP_200_OK)
    # samir:
    # def UpdateUserDetails(self, request, pk=None):
    #         print("im here")
    #         user = request.user
    #         print("user from query is: ",user)
    #         arr=[]
    #         u = UserProfile.objects.get(user=user)
    #         # print("user mail is: ", u.email)
    #         print("user name is: ", u.firstName)
    #         print("user surname is: ", u.lastName)
    #         u.username=user
    #         serializers = UserProfileSerializer(u, many=False)
    #         response = {'message': 'Get', 'results': serializers.data}
    #         return Response (response, status=status.HTTP_200_OK)

#update the user's profile details 
    @action (detail=True, methods = ['POST'])
    def UpdateUserDetails(self, request, pk=None):
        
        # get the user by the authentication
        user = request.user
        # if getUserProfile get a value (len(getUserProfile) > 0) it means that 
        # this object exist in DB and the user is trying to update that object.
        getUserProfile= UserProfile.objects.filter(user=user.id)            
        try:
            # success if need to update 
            
            profile = UserProfile.objects.get(id=getUserProfile[0].id)
            print("aaabbb ",getUserProfile[0].id)
            profile.user = user
            # get the new details
            firstName = request.data['firstName']
            lastName = request.data['lastName']
            aboutMe = request.data['aboutMe']
            hobbies = request.data['hobbies']
            myGoal = request.data['myGoal']
            #insert the new details in the new object
            profile.firstName = firstName
            profile.lastName = lastName
            profile.aboutMe = aboutMe
            profile.hobbies = hobbies
            profile.myGoal = myGoal
           
            
            profile.save()
            print ("new profile is: ", profile)
            serializers = UserProfileSerializer(profile, many=False)
            response = {'message': 'Updated', 'results': serializers.data }
            return Response (response, status=status.HTTP_200_OK)
        except:
            #requested profile not found in DB
            response = {'message': 'error'}
            return Response (response, status=status.HTTP_200_OK)
         
            
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer 

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer    

class UserCoursesViewSet(viewsets.ModelViewSet):
    queryset = UserCourses.objects.all()
    serializer_class = UserCoursesSerializer 
    authentication_classes = (TokenAuthentication, )

# get all the courses belongs to the user by the user Id
    @action (detail=True, methods = ['GET'])
    def getAllCoursesByUserId(self, request, pk=None):
        # get the user by the pk
        user = pk
        arr=[]
        userCourses= UserCourses.objects.filter(user=user)
        for userCourse in userCourses:
            serializers = UserCoursesSerializer(userCourse, many=False)
            arr.append(serializers.data)
            
        response = {'message': 'Get', 'results': arr }
        return Response (response, status=status.HTTP_200_OK)

# get all the courses belongs to the user by the token
    @action (detail=True, methods = ['GET'])
    def getAllUserCourses(self, request, pk=None):
        # get the user by the authentication
        user = request.user
        arr=[]
        userCourses= UserCourses.objects.filter(user=user.id)
        for userCourse in userCourses:
            serializers = UserCoursesSerializer(userCourse, many=False)
            arr.append(serializers.data)
            
        response = {'message': 'Get', 'results': arr }
        return Response (response, status=status.HTTP_200_OK)

    @action (detail=True, methods = ['POST'])
    def getUserCourses(self, request, pk=None):
        # get the user by the authentication
        user = request.user
        arr=[]
        userCourses= UserCourses.objects.filter(user=user.id, course=pk)
        for userCourse in userCourses:
            serializers = UserCoursesSerializer(userCourse, many=False)
            arr.append(serializers.data)
            
        response = {'message': 'Get', 'results': arr }
        return Response (response, status=status.HTTP_200_OK)

    #  Update or create a userLessons 
    @action (detail=True, methods = ['POST'])
    def addUserCourses(self, request, pk=None):
        # get the user by the authentication
        user = request.user
        # if addUserCourses get a value (len(getUserLessons) > 0) it means that 
        # this object exist in DB and the user is trying to update that object.
        getUserCourses= UserCourses.objects.filter(user=user.id, course=pk)       
                
        try:
            # success if need to update 
            course = UserCourses.objects.get(id=getUserCourses[0].id)
            # print("printing: ",lesson.notes, lesson.answer)
            course.user = user
            # user trying to change the lesson
            if 'lesson' in request.data:
                lesson = request.data['lesson']
                course.numOfLesson = lesson
           
            
            course.save()
            print ("user is: ", user)
            serializers = UserCoursesSerializer(course, many=False)
            response = {'message': 'Updated', 'results': serializers.data }
            return Response (response, status=status.HTTP_200_OK)
        except:
            # need to create
            print("trying to create")
            print("pk ", pk)
            # user began a new course
            if 'lesson' in request.data:
                lesson = request.data['lesson']
           
               
            course = Course.objects.get(id=pk)
            courseVar = UserCourses.objects.create(user=user, course=course, numOfLesson=int(lesson))
            courseVar.save()
            print("course is: ", course)
            print(lesson)
            print(type(lesson))
            response = {'message': 'created', 'results': courseVar }
            return Response (response, status=status.HTTP_200_OK)

class UserLessonsViewSet(viewsets.ModelViewSet):
    queryset = UserLessons.objects.all()
    serializer_class = UserLessonsSerializer     
    authentication_classes = (TokenAuthentication, )
     
    # #  Get all the userLessons details belonged to the requsted user by the authentication
    # @action (detail=True, methods = ['GET'])
    # def getUserLessons(self, request, pk=None):
    #     # get the user by the authentication
    #     user = request.user
    #     arr=[]
    #     userlessons= UserLessons.objects.filter(user=user.id)
    #     for userlesson in userlessons:
    #          serializers = UserLessonsSerializer(userlesson, many=False)
    #          arr.append(serializers.data)
            
    #     response = {'message': 'Get', 'results': arr }
    #     return Response (response, status=status.HTTP_200_OK)

 #  Get all the userLessons details belonged to the requsted user by the authentication
    @action (detail=True, methods = ['POST'])
    def getUserLessons(self, request, pk=None):
        # get the user by the authentication
        user = request.user
        # lessonID = '4'
        if 'lesson' in request.data:
            lessonID = request.data['lesson']
        # else:
            # lessonID=4
        arr=[]
        userlessons= UserLessons.objects.filter(user=user.id, lesson=lessonID)
        for userlesson in userlessons:
             serializers = UserLessonsSerializer(userlesson, many=False)
             arr.append(serializers.data)
            
        response = {'message': 'Get', 'results': arr }
        return Response (response, status=status.HTTP_200_OK)



    #  Update or create a userLessons 
    @action (detail=True, methods = ['POST'])
    def addUserLessons(self, request, pk=None):
        # get the user by the authentication
        user = request.user
        # if getUserLessons get a value (len(getUserLessons) > 0) it means that 
        # this object exist in DB and the user is trying to update that object.
        getUserLessons= UserLessons.objects.filter(user=user.id, lesson=pk)       
                
        try:
            # success if need to update 
            lesson = UserLessons.objects.get(id=getUserLessons[0].id)
            print("printing: ",lesson.notes, lesson.answer)
            lesson.user = user
            # user trying to change the note
            if 'notes' in request.data:
                notes = request.data['notes']
                lesson.notes = notes
             # user trying to change the answer
            if 'answer' in request.data:
                answer = request.data['answer']
                lesson.answer = answer
            
            lesson.save()
            print ("user is: ", user)
            serializers = UserLessonsSerializer(lesson, many=False)
            response = {'message': 'Updated', 'results': serializers.data }
            return Response (response, status=status.HTTP_200_OK)
        except:
            # need to create
            print("trying to create")
            print("pk ", pk)
            # user trying to create a note
            if 'notes' in request.data:
                notes = request.data['notes']
                answer = ""
            # user trying to create an answer
            if 'answer' in request.data:
                answer = request.data['answer']
                notes = ""
               
            lesson = Lesson.objects.get(id=pk)
            lessonVar = UserLessons.objects.create(user=user,lesson=lesson, answer=answer, notes=notes )
            lessonVar.save()
            response = {'message': 'created', 'results': lessonVar }
            return Response (response, status=status.HTTP_200_OK)

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer 

    # get all the students of a class
    @action (detail=True, methods = ['POST'])
    def getClassStudents(self, request, pk=None):
     
        arr=[]
        userProfile= UserProfile.objects.filter(studentClasses=pk)
        for userProfile in userProfile:
             serializers = UserProfileSerializer(userProfile, many=False)
             arr.append(serializers.data)
            
        response = {'message': 'Get', 'results': arr }
        return Response (response, status=status.HTTP_200_OK)

    # get all the teachers of a class
    @action (detail=True, methods = ['POST'])
    def getClassTeachers(self, request, pk=None):
     
        arr=[]
        userProfile= UserProfile.objects.filter(teacherClasses=pk)
        for userProfile in userProfile:
             serializers = UserProfileSerializer(userProfile, many=False)
             arr.append(serializers.data)
            
        response = {'message': 'Get', 'results': arr }
        return Response (response, status=status.HTTP_200_OK)

     # get all the coordinators of a class
    @action (detail=True, methods = ['POST'])
    def getClassCoordinators(self, request, pk=None):
     
        arr=[]
        userProfile= UserProfile.objects.filter(coordinatorClasses=pk)
        for userProfile in userProfile:
             serializers = UserProfileSerializer(userProfile, many=False)
             arr.append(serializers.data)
            
        response = {'message': 'Get', 'results': arr }
        return Response (response, status=status.HTTP_200_OK)

    #  Add a user to class 
    @action (detail=True, methods = ['POST'])
    def addUserToClass(self, request, pk=None):
        # get the class by pk
        getUserClass= Class.objects.get(id=pk)  

        # trying to add a student
        if 'student' in request.data:   
            # get the username by the data
            username = request.data['student']
            # get the user by the given username
            user = UserProfile.objects.get(username=username)
            getUserClass.students.add(user)

        # trying to add a teacher
        if 'teacher' in request.data:   
            # get the username by the data
            username = request.data['teacher']
            # get the user by the given username
            user = UserProfile.objects.get(username=username)
            getUserClass.teachers.add(user)

         # trying to add a coordinator
        if 'coordinator' in request.data:   
            # get the username by the data
            username = request.data['coordinator']
            # get the user by the given username
            user = UserProfile.objects.get(username=username)
            getUserClass.coordinators.add(user)

        getUserClass.save()
        serializers = ClassSerializer(getUserClass, many=False)
        response = {'message': 'Updated', 'results': serializers.data }
        return Response (response, status=status.HTTP_200_OK)

#  remove user from class
    @action (detail=True, methods = ['POST'])
    def removeUserFromClass(self, request, pk=None):
        # get the class by pk
        getUserClass= Class.objects.get(id=pk)  

        # trying to remove a student
        if 'student' in request.data:   
            # get the username by the data
            username = request.data['student']
            # get the user by the given username
            user = UserProfile.objects.get(username=username)
            getUserClass.students.remove(user)

        # trying to remove a teacher
        if 'teacher' in request.data:   
            # get the username by the data
            username = request.data['teacher']
            # get the user by the given username
            user = UserProfile.objects.get(username=username)
            getUserClass.teachers.remove(user)

         # trying to remove a coordinator
        if 'coordinator' in request.data:   
            # get the username by the data
            username = request.data['coordinator']
            # get the user by the given username
            user = UserProfile.objects.get(username=username)
            getUserClass.coordinators.remove(user)

        getUserClass.save()
        serializers = ClassSerializer(getUserClass, many=False)
        response = {'message': 'Updated', 'results': serializers.data }
        return Response (response, status=status.HTTP_200_OK)
    
       
               
       

    # class UserProfileViewSet(viewsets.ModelViewSet):
    #     queryset = UserProfile.objects.all()
    #     serializer_class = UserProfileSerializer 
        # authentication_classes = (TokenAuthentication, )

    # @action (detail=True, methods = ['POST'])
    # def getUserDetails(self, request, pk=None):
    #         print("im here in get user details")
    #         user = request.user
    #         print("user from query is: ", user)
    #         arr=[]
    #         u = User.objects.get(username='yarinAAA')
    #         print("user mail is: ", u.email)
    #         print("user name is: ", u.name)
    #         print("user surname is: ", u.lastName)
    #         userDetails= User.objects.filter(user=user.id, course=pk)
    #         for userCourse in userCourses:
    #             serializers = UserCoursesSerializer(userCourse, many=False)
    #             arr.append(serializers.data)
                
    #         response = {'message': 'Get', 'results': arr }
    #         return Response (response, status=status.HTTP_200_OK)

    # getStudents.append(getUserClass.students.all()) 