from flask import Flask,jsonify,request

app=Flask(__name__)

students =[
    {
        'id':1,
        'name':'anirudh',
        'surname':'duggineni',
        'age':24
    },
    {
        'id':2,
        'name':'sai',
        'surname':'duggineni',
        'age':25
    }
]

@app.route('/students', methods=['GET'])
def get_student():
    return jsonify(students)

#get students 
@app.route('/students/<int:student_id>', methods=['GET'])
def get_students(student_id):
    student=next(( student for student in students if student['id'] == student_id),None)

    if student:
        return jsonify(student)
    else:
        return jsonify({'message':'not student recorded'}),404

#post created book
@app.route('/students',methods=['POST'])
def create_student():
    new_student={
        'age':request.json['age'],
        'id':len(students)+1,
        'name':request.json['name'],
        'surname':request.json['surname']
    }
    students.append(new_student)
    return jsonify({'message':'new student recoed is created','student':new_student}),201
#post update new book
@app.route('/students/<int:student_id>',methods=['POST'])
def update_students(student_id):
    student= next((student for student in students if student['id']==student_id),None)

    if student:
        student['age']=request.json.get('age',student['age'])
        student['id']=request.json.get('id',student['id'])
        student['name']=request.json.get('name',student['name'])
        student['surname']=request.json.get('surname',student['surname'])
        return jsonify({'message':'updated the student list','student':student})
    else:
        return jsonify({'message':'not updated'}),404
#delete the student
@app.route('/student/<int:student_id>',methods=['DELETE'])
def delete_student(student_id):
    student= next((student for student in students if student['id']==student_id),None)
    if student:
        students.remove(student)
        return jsonify({'message':'successfully deleted'})
    else:
        return jsonify({'message':'not deleted'}),404
    
if __name__ == '__main__':
    app.run(debug=True)