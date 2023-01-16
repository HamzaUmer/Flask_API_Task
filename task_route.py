from flask import Blueprint
from controller.task import top_category_and_leaf
from controller.checkController import top_category

task_bp = Blueprint('task_bp', __name__)

#Create Customer APIs
task_bp.route('/top_category_and_leaf', methods=['POST'])(top_category_and_leaf)

task_bp.route('/top_category', methods=['POST'])(top_category)


