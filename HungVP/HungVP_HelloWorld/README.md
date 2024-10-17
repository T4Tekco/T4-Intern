## API Endpoints Documentation  for testing 

### LESSON MODEL
* `GET: /api/lessons` : Get all lessons
  
  Result:
  ```
  {
    "timestamp": "2024-10-17T14:23:51.365217",
    "status": 200,
    "message": "Lessons retrieved successfully",
    "result": [
         {
            "id": 2,
            "name": "Lập trình OOP nâng cao",
            "is_active": true
        },
        {
            "id": 3,
            "name": "Lập trình Odoo căn bản",
            "is_active": false
        },
        {
            "id": 4,
            "name": "Lâp trình Odoo căn bản",
            "is_active": false
        }
    ]
  }
  ```
* `GET: /api/lessons/{lesson_id}` : Get lesson by lesson_id

  Result:
  ```
  {
      "timestamp": "2024-10-17T14:24:07.535520",
      "status": 200,
      "message": "Lesson retrieved successfully",
      "result": {
          "id": 3,
          "name": "Lập trình Odoo căn bản",
          "is_active": false
      }
  }
  ```
* `POST: /api/lesson` : Create new a lesson
  
  Request data: 
    ```
  {
      "name": "Photoshop cơ bản",
      "is_active": true
  }
    ```
  Result:
  ```
  {
      "timestamp": "2024-10-17T15:10:49.345949",
      "status": 200,
      "message": "Lesson already exists",
      "result": {
          "id": 13,
          "name": "Photoshop cơ bản",
          "is_active": true
      }
  }
  ```

* `PUT: /api/lessons/{lesson_id}` : Update lesson by lesson_id
  
    Request data: 
   ```
   {
      "name": "Photoshop nâng cao",
      "is_active": false
   }
   ```
    Result:
  ```
  {
      "timestamp": "2024-10-17T15:14:58.316319",
      "status": 200,
      "message": "Lesson updated successfully",
      "result": {
          "id": 13,
          "name": "Photoshop nâng cao",
          "is_active": false
      }
  }
  ```

* `DELETE: /api/lessons/{lesson_id}` : Delete lesson by course_id

   Result:
  ```
  {
      "timestamp": "2024-10-17T15:20:48.803616",
      "status": 200,
      "message": "Lesson deleted successfully",
      "result": null
  }
   ```

### COURSE MODEL
* `GET: /api/courses` : Get all courses

    Result:
  ```
  {
      "timestamp": "2024-10-17T15:22:41.938778",
      "status": 200,
      "message": "Courses retrieved successfully",
      "result": [
          {
              "id": 1,
              "name": "Lập trình viên Java",
              "is_active": true
          },
          {
              "id": 2,
              "name": "Lập trình viên Odoo",
              "is_active": true
          },
          {
              "id": 3,
              "name": "Designer",
              "is_active": true
          }
      ]
  }
  ```
* `GET: /api/courses/{course_id}` : Get course by course_id
  
    Result:
  ```
  {
      "timestamp": "2024-10-17T15:23:15.437263",
      "status": 200,
      "message": "Course found with course_id: 1",
      "result": {
          "id": 1,
          "name": "Lập trình viên Java",
          "is_active": true
      }
  }
  ```
* `POST: /api/lesson` : Create new a course
  
  Request data: 
```
  {
        "name": "Dạy làm giàu",
        "is_active": true
  }
```

 Result:
  ```
  {
        "timestamp": "2024-10-17T15:23:56.839789",
        "status": 201,
        "message": "Course created successfully",
        "result": {
            "id": 4,
            "name": "Dạy làm giàu",
            "is_active": true
      }
  }
  ```
* `PUT: /api/courses/{course_id}` : Update course by course_id
  
    Request data: 
```
    {
        "name": "Dạy làm nghèo :v",
        "is_active": true
    }
```

 Result:
  ```
  {
        "timestamp": "2024-10-17T15:25:19.205145",
        "status": 200,
        "message": "Course updated successfully",
        "result": {
            "id": 4,
            "name": "Dạy làm nghèo :v",
            "is_active": true
      }
  }
  ```
* `DELETE: /api/courses/{course_id}` : Delete course by course_id

 Result:
```
  {
      "timestamp": "2024-10-17T15:26:08.284150",
      "status": 200,
      "message": "Course deleted successfully",
      "result": null
  }
```
