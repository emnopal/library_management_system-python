if __name__ == '__main__':
    try:
        import os
        os.system('uvicorn api.main_api:app --reload --port 5500')
    except KeyboardInterrupt:
        print("Session ended, run python main.py to run the app again")
    except ImportError:
        os.system('python -m pip install -r requirements.txt')
    except:
        print("""
        Error: There is unexpected error.
        Please check the following issues:
            1. Error: uvicorn is not installed:
                Please install uvicorn with:
                    python -m pip install uvicorn
            2. Error: there is conflict with another program or port:
                Check the running apps, or check the port. Maybe port 5500 is used by another running process
            3. Error: uvicorn conflicts:
                run python -m pip install uvicorn --upgrade
                or run python -m pip install uvicorn --upgrade --user
                or run python -m pip install uvicorn --upgrade --user --force-reinstall
        """)