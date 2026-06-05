from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    success = request.args.get('success', False)
    return render_template('contact.html', success=success)

@app.route('/submit_inquiry', methods=['POST'])
def submit_inquiry():
    name = request.form.get('name')
    phone = request.form.get('phone')
    property_type = request.form.get('property_type')
    message = request.form.get('message')
    
    # Save data to text file securely
    with open('inquiries.txt', 'a', encoding='utf-8') as f:
        f.write(f"Name: {name} | Phone: {phone} | Type: {property_type} | Message: {message}\n")
        f.write("-" * 50 + "\n")
        
    # Redirect back to contact page with success state
    return redirect(url_for('contact', success='true'))

if __name__ == '__main__':
    # Render port automatic allocate karta hai, isliye host aur port dynamic hona chahiye
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)