## API Endpoints Documentation  for tesing 

### Lesson model
* `GET: /api/lessons` : Get all lessons
* `GET: /api/lessons/{lesson_id}` : Get lesson by lesson_id
* `POST: /api/lesson` : Create new a lesson
   request_data: 
    {
        "name": "Lập trình hướng đối tượng OOP",
        "is_active": true
    }

* `PUT: /api/lessons/{lesson_id}` : Update lesson by lesson_id
    request_data: 
    {
        "name": "Lập trình hướng đối tượng OOP",
        "is_active": true
    }

* `DELETE: /api/lessons/{lesson_id}` : Delete lesson by course_id 

### Course model
* `GET: /api/courses` : Get all courses
* `GET: /api/courses/{course_id}` : Get course by course_id
* `POST: /api/lesson` : Create new a course
   request_data: 
    {
        "name": "Lập trình viên Java",
        "is_active": true
    }

* `PUT: /api/courses/{course_id}` : Update course by course_id
    request_data: 
    {
        "name": "Lập trình viên Java",
        "is_active": true
    }

* `DELETE: /api/courses/{course_id}` : Delete course by course_id