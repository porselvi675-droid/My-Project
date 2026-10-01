from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('home_planner'))

@app.route('/dashboard')
def dashboard():
    return redirect(url_for('home_planner'))

# ---------------- 1. HOME BUDGET ----------------
@app.route('/home_planner')
def home_planner():
    return render_template('home_planner.html')

@app.route('/home_result', methods=['POST', 'GET'])
def home_result():
    total_budget = 5000.0
    if request.method == 'POST':
        try:
            total_budget = float(request.form.get('total_budget', 5000))
        except:
            total_budget = 5000.0

    categories = [
        {
            'name': 'Home Lighting & Electricals',
            'allocation': total_budget * 0.35,
            'items': [
                {'name': 'LED Bulbs & Smart Lights', 'desc': 'Energy-efficient LED lighting setup', 'price': total_budget * 0.20, 'qty': 1},
                {'name': 'Wiring & Switchboards', 'desc': 'Modular switches and copper wiring', 'price': total_budget * 0.15, 'qty': 1}
            ]
        },
        {
            'name': 'Home Cooling & Fans',
            'allocation': total_budget * 0.35,
            'items': [
                {'name': 'High-Speed Ceiling Fans', 'desc': 'Energy-saving ceiling fans', 'price': total_budget * 0.35, 'qty': 2}
            ]
        },
        {
            'name': 'Living Room Furniture',
            'allocation': total_budget * 0.30,
            'items': [
                {'name': 'Chairs & Coffee Table', 'desc': 'Comfortable seating setup', 'price': total_budget * 0.30, 'qty': 1}
            ]
        }
    ]

    return render_template(
        'home_result.html',
        page_title="Your Personalized Home Budget Plan",
        total_budget=total_budget,
        remaining_budget=0.0,
        categories=categories
    )

# ---------------- 2. PARTY BUDGET ----------------
@app.route('/party_planner')
def party_planner():
    return render_template('party_planner.html')

@app.route('/party_result', methods=['POST', 'GET'])
def party_result():
    total_budget = 5000.0
    guest_count = 50
    venue_type = 'Banquet Hall'

    if request.method == 'POST':
        try:
            total_budget = float(request.form.get('total_budget', 5000))
        except:
            total_budget = 5000.0
        try:
            guest_count = int(request.form.get('guest_count', 50))
        except:
            guest_count = 50
        venue_type = request.form.get('venue_type', 'Banquet Hall') or 'Banquet Hall'

    categories = [
        {
            'name': 'Catering & Food Services',
            'allocation': total_budget * 0.50,
            'items': [
                {'name': 'Party Buffet Dinner', 'desc': f'Full course meal for {guest_count} guests', 'price': (total_budget * 0.50) / max(guest_count, 1), 'qty': guest_count}
            ]
        },
        {
            'name': 'Venue Rental & Setup',
            'allocation': total_budget * 0.30,
            'items': [
                {'name': f'{venue_type} Booking', 'desc': 'Venue rental fee and setup charges', 'price': total_budget * 0.30, 'qty': 1}
            ]
        },
        {
            'name': 'Party Decoration & Music',
            'allocation': total_budget * 0.20,
            'items': [
                {'name': 'Stage & Entrance Decoration', 'desc': 'Balloons, flowers, and lighting stage', 'price': total_budget * 0.12, 'qty': 1},
                {'name': 'Party DJ & Audio System', 'desc': 'Sound system and DJ setup', 'price': total_budget * 0.08, 'qty': 1}
            ]
        }
    ]

    return render_template(
        'home_result.html',
        page_title="Your Personalized Party Budget Plan",
        total_budget=total_budget,
        remaining_budget=0.0,
        categories=categories
    )

# ---------------- 3. JEWELRY BUDGET ----------------
@app.route('/jewelry_planner')
def jewelry_planner():
    return render_template('jewelry_planner.html')

@app.route('/jewelry_result', methods=['POST', 'GET'])
def jewelry_result():
    total_budget = 5000.0
    metal_type = '22K Gold'

    if request.method == 'POST':
        try:
            total_budget = float(request.form.get('total_budget', 5000))
        except:
            total_budget = 5000.0
        metal_type = request.form.get('metal_type', '22K Gold') or '22K Gold'

    categories = [
        {
            'name': f'{metal_type} Necklaces & Sets',
            'allocation': total_budget * 0.50,
            'items': [
                {'name': f'{metal_type} Designer Chain / Necklace', 'desc': 'Custom handcrafted design', 'price': total_budget * 0.50, 'qty': 1}
            ]
        },
        {
            'name': f'{metal_type} Bangles Collection',
            'allocation': total_budget * 0.30,
            'items': [
                {'name': f'{metal_type} Traditional Bangles', 'desc': 'Set of matching designer bangles', 'price': total_budget * 0.30, 'qty': 2}
            ]
        },
        {
            'name': f'{metal_type} Rings & Accessories',
            'allocation': total_budget * 0.20,
            'items': [
                {'name': f'{metal_type} Finger Ring', 'desc': 'Matching stone/plain ring', 'price': total_budget * 0.20, 'qty': 1}
            ]
        }
    ]

    return render_template(
        'home_result.html',
        page_title="Your Personalized Jewelry Budget Plan",
        total_budget=total_budget,
        remaining_budget=0.0,
        categories=categories
    )

if __name__ == '__main__':
    app.run(debug=True)