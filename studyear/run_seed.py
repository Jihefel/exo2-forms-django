import django
django.setup()

from stud_app.seed import run

if __name__== '__main__':
    run()
