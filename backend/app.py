from flask import Flask, render_template, Response, request, redirect
from pose_left import generate_frames
from pose_right import right_curl
from pose_pushup import pushup
from pose_squat import squat
from pose_kneetaps import kneetaps
from pose_op import op
from pose_lunges import lunges
import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

app = Flask(__name__)


# Redirect '/' to '/api'
@app.route('/')
def home():
    return redirect('/api')

@app.route('/api', methods = ['GET'])
def index():
    return render_template('request_page.html')

# @app.route('/video_feed_left')
# def video_feed_left():
#     return Response(left_curl(),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/video_feed_left')
def video_feed_left():
    return Response(generate_frames(target_reps=10, target_sets=3), 
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_right')
def video_feed_right():
    return Response(right_curl(target_reps=10, target_sets=3),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_pushup')
def video_feed_pushup():
    return Response(pushup(target_reps=10, target_sets=3),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_squat')
def video_feed_squat():
    return Response(squat(target_reps=10, target_sets=3),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/video_feed_kneetaps')
def video_feed_kneetaps():
    return Response(kneetaps(target_reps=10, target_sets=3),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_op')
def video_feed_op():
    return Response(op(target_reps=10, target_sets=3),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_lunges')
def video_feed_lunges():
    return Response(lunges(target_reps=10, target_sets=3),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/show')
def show():
    subject = request.args.get('sub')
    return redirect(f'/video_feed_{subject}')

if __name__ == '_main_':
    app.run(host = "0.0.0.0" , debug=False)
# from flask import Flask, Response, request, redirect, jsonify
# from pose_left import left_curl
# from pose_right import right_curl
# from pose_pushup import pushup
# from pose_squat import squat
# import cv2

# app = Flask(_name_)

# # Redirect '/' to '/api'
# @app.route('/')
# def home():
#     return jsonify({"message": "Welcome to the Pose Detection API!"})

# @app.route('/api', methods=['GET'])
# def index():
#     return jsonify({"message": "Use endpoints like /video_feed_left, /video_feed_right, etc."})

# @app.route('/video_feed_left')
# def video_feed_left():
#     return Response(left_curl(), mimetype='multipart/x-mixed-replace; boundary=frame')

# @app.route('/video_feed_right')
# def video_feed_right():
#     return Response(right_curl(), mimetype='multipart/x-mixed-replace; boundary=frame')

# @app.route('/video_feed_pushup')
# def video_feed_pushup():
#     return Response(pushup(), mimetype='multipart/x-mixed-replace; boundary=frame')

# @app.route('/video_feed_squat')
# def video_feed_squat():
#     return Response(squat(), mimetype='multipart/x-mixed-replace; boundary=frame')

# @app.route('/show')
# def show():
#     subject = request.args.get('sub')
#     return redirect(f'/video_feed_{subject}')

# if _name_ == '_main_':
#     app.run(host="0.0.0.0", debug=False)