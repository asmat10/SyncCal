# Installation und Nutzungsanleitung

## 1. Vorbereitung PIP

```python
# installiere die aktuellste pip version (23.2.1)
pip3 install --upgrade pip
python -m pip install --upgrade pip
# installiere/aktualisiere alle notwendigen Pakete
pip install requests
pip install google-auth
pip install google-auth-oauthlib
pip install google-auth-httplib2
pip install google-api-python-client
```

## 2. Vorbereitung MongoDB
blub

## 3. Software Architektur
blub

## 4. DB ERM/ERP Modell
blub

## 5. Knwon Issues

### 5.1 PIP Installations und Update Probleme (SSL oder Versions konflikt)

#### 5.1.1 [Windows] Use a Virtual Environment: It's a good practice to create and use virtual environments for your Python projects. This isolates your project's dependencies from the system-wide Python installation and can prevent conflicts.

To create a virtual environment, open a Command Prompt, navigate to your project directory, and run:

```python
python -m venv venv
```
Then, activate the virtual environment:
On Windows:

```python
venv\Scripts\activate
```
Once the virtual environment is active, you can install packages without affecting the system-wide Python installation.