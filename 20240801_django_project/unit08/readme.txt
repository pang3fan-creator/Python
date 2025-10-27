
假设有以下列表 

users = [1,3,5],用于存储学生的ID

class = [{'id':1,'name':'语文'},{'id':2,'name':'数学'},{'id':3,'name':'英语'}],用于存储课程的ID及名称

以下列表代表学生各科的成绩
scores = [
    {
     	"student_id":1,
     	"class_id":1,
     	"score":80,
    },
     {
     	"student_id":1,
     	"class_id":2,
     	"score":89,
    },
     {
     	"student_id":1,
     	"class_id":3,
     	"score":92,
    },
     {
     	"student_id":2,
     	"class_id":1,
     	"score":92,
    },
      {
     	"student_id":2,
     	"class_id":2,
     	"score":92,
    },
      {
     	"student_id":2,
     	"class_id":3,
     	"score":92,
    },
     {
     	"student_id":3,
     	"class_id":1,
     	"score":92,
    },
      {
     	"student_id":3,
     	"class_id":2,
     	"score":92,
    },
      {
     	"student_id":3,
     	"class_id":3,
     	"score":92,
    },
]



请形成如果结构

[
	{ 1: {'数学':82,'语文':82,'英语':82}},
	{ 3: {'语文':82,'数学':82,'英语':82}},
	{ 5: {'语文':82,'数学':82,'英语':82}},
]

[
	{1: {'语文': 'B', '数学': 'B', '英语': 'B'}}, 
	{3: {'语文': 'B', '数学': 'B', '英语': 'B'}},
 	{5: {'语文': 'B', '数学': 'B', '英语': 'B'}}
 ]

