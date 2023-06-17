# hr-test-python

This is the interview questions for python dev skills.

---
### 1. How do you setup local python dev environment?  
- What IDE do you use?
  - VS Code or PyCharm
- How do you setup python production environment in Linux?
  - List the cli commands if possible.
   1. Update the package lists by running: `sudo apt update`
   2. Install Python: `sudo apt install python3`
   3. Install pip: `sudo apt install python3-pip`
   4. Set up a virtual environment: `sudo apt install python3-venv`  `python3 -m venv myenv`
   5. Activate the virtual environment: `source myenv/bin/activate`
   6. Install project dependencies: `pip install -r requirements.txt`
   7. Depending on the project's requirements, install additional tools
   8. Verify the setup by running: `python --version`, `pip --version`

---
### 2. Are you familiar using any linux distro?
- Yes
  - crontab: The crontab command is used to manage cron jobs in Linux. It's a time-based job scheduler that allows you to schedule and automate tasks to run at specific intervals.
  - ssh: SSH (Secure Shell) is a network protocol that provides secure remote access to a Linux system. It allows you to log in and access a remote server over an encrypted connection.
  - nfs: NFS (Network File System) is a distributed file system protocol that allows a user on a client computer to access files over a network as if they were on the local system. With NFS, you can share directories from a server and mount them on client machines, enabling file sharing and centralized storage.
  - nginx: Nginx is a web server and reverse proxy server. It's known for its high performance, scalability, and efficient handling of concurrent connections. Nginx is often used as a web server to serve static files or as a reverse proxy to distribute incoming requests to multiple backend servers.

---
### 3. Setup a RESTful API with python & nginx.
- Using localhost
- Free to choose any python web component
- All outputs in JSON

API definition: /timestamp
> return current UNIX timestamp
```
# Test command:
curl 127.0.0.1/timestamp

# Expected outcome:
{"timestamp":1624900201}
```

API definition: /readdata
> read POST JSON input and send it back
```
# Test command:
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"username":"abc","password":"xyz"}' \
  http://127.0.0.1/readdata

# Expected outcome:
{"username":"abc","password":"xyz"}
```

bad input
```
# Test command:
curl 127.0.0.1/noexist

# Expected outcome:  (404)
... 
404 Not Found 
...
```

#### What to submit:
- Python code
 - The Python code is in a `api.py` file that's included in the root-level directory of this branch
---
### 3.1 Nginx (Optional)
- Use Nginx as the front web server (reverse proxy)
- deploy python program on port 8000

#### What to submit:
- Nginx server config
 - The Nginx server config is in a `nginx.conf` file that is included in root-level directory of this branch
