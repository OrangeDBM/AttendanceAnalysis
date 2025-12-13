# Attendance Analysis

## Features:

### 1. Login Function

By creating a user password table, the system matches the username and password entered on the front-end page with the username and password fields in the database's user table during login.  Successful login routes to the analysis page, while failed login routes back to the login page.

### 2. Flask API Functionality

Provides a convenient API KEY and parameter passing mechanism for real-time URL calls to perform data analysis using MySQL stored procedures in the backend and return results (in JSON format).

### 3. Flask Parameter Passing and MySQL Stored Procedure Analysis

Connects to the backend MySQL database, fully utilizing SQL capabilities to build powerful data analysis functions.  It leverages Flask's front-end interaction and the backend database's SQL analysis capabilities, separating computation and presentation and fully utilizing the database's inherent computing power to build a simple yet powerful data analysis platform.

### 4. Real-time Analysis and Download

By entering the required parameters, the parameters are passed to the MySQL stored procedure. The stored procedure then calculates the results, assembles the data into an Excel file, and allows the user to download it to their local machine via the webpage.




## 功能如下

### 1.登陆功能

通过建立用户密码表，登陆时通过前端页面输入用户和密码与数据库用户表里的用户名字段和密码字段进行匹配，成功即路由分析页面，失败路由登陆页面

### 2.Flask API功能

方便实用API KEY 加传参即时调用URL进行后台MySQL存储过程数据分析并返回结果（JSON格式）

### 3.Flask 传参调用MySQL存储过程分析

与后端MySQL数据库相联，充分使用SQL能力建立强大的数据分析功能，充分使用Flask前端交互和后端数据库SQL分析能力，把计算和展示分开并充分发挥数据库自身的计算能力，构建简单强大的数据分析平台

### 4.即时分析，即时下载

通过输入需要的传人参数，将参数带入MySQL存储过程，然后将存储过程计算结果把数据组装成EXCEL通过网页下载到本地
