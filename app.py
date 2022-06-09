from flask import Flask, render_template, request


app=Flask(__name__)

feedbacks=[]

sold=[]

produits=[
  {
    "categorie": "Orinateur portable", 
    "description": "Lorem ipsum dolor sit, amet consecipsum dolor sit, amet consectetur adipisicing elit. Et necessitatibus sunt alias nostrum quisquam ut commodi. Officia doloribus dolorem, doloremque, vero aliquam veritatis iure quae nihil, earum porro itaque quam.", 
    "id": 1, 
    "image": "1.jpeg", 
    "marque": "DELL", 
    "model": "Inspiron latitude", 
    "prix": 6840, 
    "qtt": 6
  }, 
  {
    "categorie": "Orinateur portable", 
    "description": "Lorem ipsum dolor sit, amet consecipsum dolor sit, amet consectetur adipisicing elit. Et necessitatibus sunt alias nostrum quisquam ut commodi. Officia doloribus dolorem, doloremque, vero aliquam veritatis iure quae nihil, earum porro itaque quam.", 
    "id": 2, 
    "image": "2.jpeg", 
    "marque": "DELL", 
    "model": "Inspiron", 
    "prix": 5200, 
    "qtt": 4
  }, 
  {
    "categorie": "Orinateur portable", 
    "description": "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Et necessitatibus sunt alias nostrum quisquam ut commodi. Officia doloribus dolorem, doloremque, vero aliquam veritatis iure quae nihil, earum porro itaque quam.", 
    "id": 3, 
    "image": "3.jpeg", 
    "marque": "HP", 
    "model": "Elitbook 40", 
    "prix": 4500, 
    "qtt": 32
  }, 
  {
    "categorie": "Orinateur portable", 
    "description": "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Et necessitatibus sunt alias nostrum quisquam ut commodi. Officia doloribus dolorem, doloremque, vero aliquam veritatis iure quae nihil, earum porro itaque quam.", 
    "id": 4, 
    "image": "4.jpeg", 
    "marque": "LENOVO", 
    "model": "X1 Yoga", 
    "prix": 8800, 
    "qtt": 2
  }, 
  {
    "categorie": "Orinateur portable", 
    "description": "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Et necessitatibus sunt alias nostrum quisquam ut commodi. Officia doloribus dolorem, doloremque, vero aliquam veritatis iure quae nihil, earum porro itaque quam.", 
    "id": 5, 
    "image": "5.jpeg", 
    "marque": "LENOVO", 
    "model": "X280", 
    "prix": 12000, 
    "qtt": 4
  }, 
  {
    "categorie": "Orinateur portable", 
    "description": "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Et necessitatibus sunt alias nostrum quisquam ut commodi. Officia doloribus dolorem, doloremque, vero aliquam veritatis iure quae nihil, earum porro itaque quam.", 
    "id": 6, 
    "image": "6.jpeg", 
    "marque": "APEL", 
    "model": "Macbook pro", 
    "prix": 20000, 
    "qtt": 1
  }, 
  {
    "categorie": "Orinateur portable", 
    "description": "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Et necessitatibus sunt alias nostrum quisquam ut commodi. Officia doloribus dolorem, doloremque, vero aliquam veritatis iure quae nihil, earum porro itaque quam.", 
    "id": 7, 
    "image": "7.jpeg",
    "marque": "APPEL", 
    "model": "Macbook air", 
    "prix": 6800, 
    "qtt": 42
  }
]

@app.route("/")
def index():
    return render_template("index.html",product=produits,sold=sold)

@app.route("/add/<image>/<int:id>/<marque>/<model>")
def add(id,marque,model,image):
  op={"image":image, "marque":marque, "model":model, "id":id}
  sold.append(op)
  return render_template("index.html", product=produits, sold=sold)

@app.route("/remove/<int:id>")
def remove(id):
  sold.pop(id)
  print(sold)
  return render_template("panier.html",product=produits,sold=sold)


@app.route("/panier")
def panier():
    return render_template("panier.html", sold=sold)


@app.route("/detail")
def detail():
    return render_template("detail.html")

@app.route("/contact",methods=["GET","POST"])
def contact():
  if request.method=="POST":
    nom=request.form.get("nom")
    email=request.form.get("mail")
    message=request.form.get("message")
    user={"nom":nom, "email":email, "message":message}
    feedbacks.append(user)
    print(feedbacks)

  if request.method=="GET":
    nom=request.args.get("nom")
    email=request.args.get("mail")
    message=request.args.get("message")
    user={"nom":nom, "email":email, "message":message}
    feedbacks.append(user)
    print(feedbacks)

  return render_template("contact.html")

if(__name__=="__main__"):
    app.run(debug=True)