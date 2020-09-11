# ToDoListAPI

The TodoListAPI provides the following features to maintain and manage your daily routine tasks
1. RESTful architecture
2. Firebase Authentication
3. Easy cookie based session management

## Here is a description of all the endpoints in brief

### 1. /allLists
This endpoint can only be called via GET method and returns all the lists for the signed in user
``` payload: nothing ```

### 2. /list
This endpoint is used for list CRUD operations. (<method>:/<path>)

#### 2.1 GET:/list/<listId>
  Used to get list with particular ID
``` payload: nothing ```
  
#### 2.2 POST:/list
  Used to add new list
  ```payload: {title: <required, string>}```
  
#### 2.3 PUT:/list
  Used to update list status to complete/incomplete
  ```payload: {listId: <required, int>}```
  
#### 2.4 DELETE:/list
  Used to delete a particular list
  ```payload: {listId: <required, int>}```
  
### 3. /task
This path is used to add, update and delete a task. (<method>:/<path>)

#### 3.1 POST:/task
  Used to add new task
  ```payload: {title: <required, string>, listId: <required, int>, dateTime: <optional, str(yyyy-mm-dd hh-mm-ss)>}```

#### 3.2 PUT:/task
  Used to update task status to complete/incomplete
  ```payload: {listId: <valid task id>}```

#### 3.3 DELETE:/task
  Used to delete a particular task
  ```payload: {listId: <valid task id>}```
  
### 4 Authentication
Following are the routes used for authentication

#### 4.1 POST:/login
  Used to login an existing user
  ```payload: {email: <registered user email>, password: <registered user password>}```
  
#### 4.2 POST:/register
  Used to register and login a new user
  ```payload: {email: <new user email>, password: <new user password>}```

