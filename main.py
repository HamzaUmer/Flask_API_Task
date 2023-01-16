from app import app
from routes.task_route import task_bp

#task
app.register_blueprint(task_bp, url_prefix='/')
        
if __name__ == "__main__":
    app.run()
