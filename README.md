# Flask API Demo

## **Prerequisites**

1. **Python**: Ensure Python 3.x is installed.  
   - Check Python version:  
     ```bash
     python --version
     # or
     python3 --version
     ```
2. **Visual Studio Code (VSCode)**: Install from [https://code.visualstudio.com/](https://code.visualstudio.com/).

3. **Thunder Client** (optional, for API testing):  
   - Install the Thunder Client VSCode extension from the Extensions Marketplace.  
   - Alternatively, you can use tools like Postman, Curl, or your browser.

---

## **Setup Instructions**

### 1. Clone or Download the Repository
Download the files or clone the repository:

```bash
git clone https://github.com/JeremiahHerring/OSS-API-DEMO
cd OSS-API-DEMO
```

### 2. Create a Virtual Environment
A virtual environment is used to isolate dependencies.

#### **Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

#### **macOS/Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies
Install Flask:

```bash
pip install flask
```

---

### 4. Run the Application
Start the Flask app by running:

```bash
python3 app.py
```

By default, the app will run on **localhost** using port **3000**.

---

## **Making API Requests**

### Base URL
```plaintext
http://localhost:3000
```

### Endpoints
- **GET `/posts`**: Retrieve all posts.
- **GET `/posts/<id>`**: Retrieve a specific post by ID.
- **POST `/posts`**: Create a new post.  
  - Example body (JSON):
    ```json
    {
        "title": "Sample Post",
        "content": "This is a demo post."
    }
    ```
- **PUT `/posts/<id>`**: Update a post by ID.  
  - Example body (JSON):
    ```json
    {
        "title": "Updated Title",
        "content": "Updated content."
    }
    ```
- **DELETE `/posts/<id>`**: Delete a post by ID.

---

### Testing with Thunder Client
1. Open VSCode and click on the **Thunder Client** icon in the Activity Bar.
2. Create a new request for any of the endpoints.
3. Specify the HTTP method (GET, POST, PUT, DELETE) and the request body (if needed).

---

## **Troubleshooting**

- **Virtual Environment Issues**:
  - If `venv` is not recognized, make sure Python is correctly installed and added to your system's PATH.

- **Port Issues**:
  - If port `3000` is in use, Flask may default to another port (e.g., `5000`). Check the terminal output to confirm the running port.

---

This setup should be sufficient to demo and interact with your API. Happy coding! 🎉
