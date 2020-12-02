# Bibb County Teacher Advocacy

## Set up

1. Clone this repository

        git clone git@github.com:ezhaohang/bibb-county-teacher-advocacy.git

2. Install virtualenvwrapper (if not already installed)

        sudo pip3 install virtualenv

3. Create virtual environment

        virtualenv venv -p python3

4. Activate virtual environment

        source venv/bin/activate

5. Install required packages

        pip3 install -r requirements.txt

6. Run project

        cd mvp
        python3 manage.py migrate
        python3 manage.py runserver

7. Deactivate virtual environment when done

        deactivate
