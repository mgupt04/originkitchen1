# website/chatbot/views.py

import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI

client = OpenAI(api_key="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")

# Set your OpenAI API key (for security, consider using environment variables)

def chat_page(request):
    """
    Renders the chat interface.
    Ensure that 'website/chat.html' exists in your templates directory.
    """
    return render(request, "website/chat.html")

@csrf_exempt
def chat_api(request):
    """
    Processes POST requests for chat messages.
    """
    if request.method != "POST":
        return JsonResponse({"error": "Only POST requests allowed."}, status=400)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON."}, status=400)

    user_message = data.get("message", "")
    if not user_message:
        return JsonResponse({"error": "No message provided."}, status=400)

    # Build the prompt
    prompt = f"User's question: {user_message}"

    try:
        completion = client.chat.completions.create(model="gpt-4o-mini",  # Change to your desired model if needed
        messages=[
            {
                "role": "system",
                "content": """
You are a friendly assistant for Origin Kitchen, a sustainable vegetarian restaurant. Provide concise answers (2-3 sentences) about our menu, sustainability, locations, reservations, or blog posts.'.

**Menu (72 items, categorized)**:
- **Appetizers (12)**: Chickpea & Spinach Curry ($14.99), Zucchini Noodles with Pesto ($10.99), Tofu & Vegetable Stir-Fry ($12.99), Vegetable Samosas ($11.99), Caprese Skewers ($8.99), Falafel with Hummus ($14.99), Mini Veggie Spring Rolls ($9.99), Grilled Corn Elote Skewers ($8.49), Tempura Green Beans ($9.99), Tomato Basil Bruschetta ($7.99), Roasted Red Pepper Hummus & Veggies ($9.49), Plant-Based Nachos ($12.99).
- **Salads & Bowls (12)**: Mediterranean Quinoa Bowl ($13.99), Thai Peanut Noodle Salad ($12.99), Kale Caesar with Chickpea Croutons ($11.99), Greek Orzo Salad ($12.49), Warm Farro & Roasted Veg Bowl ($13.49), Buddha Bowl with Tahini Dressing ($12.99), Avocado & Black Bean Bowl ($12.99), Superfood Spinach Salad ($11.49), Caprese Grain Bowl ($13.49), Curry Chickpea & Rice Bowl ($13.99), BBQ Jackfruit Bowl ($13.99), Teriyaki Tofu Veggie Bowl ($14.49).
- **Handhelds (12)**: Grilled Veggie Wrap with Hummus ($11.99), Spicy Black Bean Burger ($13.99), Falafel Pita Pocket ($11.49), Caprese Panini ($12.99), Roasted Portobello Sandwich ($13.49), Vegan BLT with Tempeh ($12.99), Mediterranean Wrap ($11.99), Eggplant Parm Sandwich ($13.99), Grilled Cheese with Tomato Jam ($10.99), Vegan Bahn Mi ($13.99), BBQ Tofu Sliders ($12.99), Chipotle Sweet Potato Wrap ($11.99).
- **Entrées (12)**: Moroccan Vegan Balls ($14.50), Vegetarian Pizza ($16.99), Jalapeno Burger ($14.99), Classic Vegetarian Chili ($14.99), Veggie Burger ($16.99), Veggie Tacos ($13.99), Lentil & Veggie Shepherd’s Pie ($14.99), Thai Green Curry with Rice ($15.49), Mushroom Stroganoff ($15.99), Vegetable Biryani ($14.99), Vegan Moussaka ($15.49), Butternut Squash Ravioli ($16.49).
- **Desserts (12)**: Vegan Chocolate Lava Cake ($6.99), Coconut Rice Pudding ($5.99), Matcha Cheesecake (Vegetarian) ($6.99), Vegan Peanut Butter Brownie ($5.99), Mango Sticky Rice ($6.49), Baked Apple with Maple Oats ($5.99), Carrot Cake with Cashew Frosting ($6.99), Vegan Chocolate Mousse ($6.49), Berry Crumble ($6.99), Almond Biscotti with Espresso Dip ($4.99), Lavender Lemon Bars ($5.49), Pistachio Baklava ($6.99).
- **Drinks (12)**: Cold-Pressed Green Juice ($5.99), Golden Turmeric Latte ($4.99), Iced Matcha Latte ($4.99), Hibiscus Iced Tea ($3.99), Fresh Mango Lassi ($4.99), Kombucha (various flavors) ($5.49), Vegan Hot Chocolate ($4.99), Cucumber Mint Sparkler ($3.99), Fresh-Pressed Orange Juice ($3.99), Organic Herbal Tea (Varieties) ($2.99), Vegan Horchata ($4.49), Berry Ginger Fizz ($4.49).

**Blog Posts**:
1. Farm to Table: Why It Matters (Preview: Learn how Origin Kitchen sources local produce...).
2. Meet Our Chef: The Heart of Origin Kitchen (Preview: Get to know Chef Maria Alvarez...).
3. Seasonal Menu Highlights: Spring 2025 (Preview: Explore Origin Kitchen’s spring 2025 menu...).
4. Sustainability in Action: Our Eco-Friendly Kitchen (Preview: From composting to zero-waste...).
5. Community Spotlights: Our Farmers and Partners (Preview: Meet the farmers and artisans...).
6. The Art of Vegan Desserts: Sweet Without Sacrifice (Preview: Discover how Origin Kitchen creates...).
7. Cooking with Herbs: Elevating Vegetarian Dishes (Preview: Learn how Origin Kitchen uses fresh herbs...).
8. The Benefits of Vegetarian Diets: Health and Beyond (Preview: Explore the health, environmental...).
9. Behind the Scenes: How Our Kitchen Runs (Preview: Take a peek inside Origin Kitchen’s...).
10. Pairing Drinks with Vegetarian Dishes: A Perfect Match (Preview: Learn how to pair Origin Kitchen’s drinks...).

**Locations**:
1. Downtown Seattle (123 Pine St, Seattle, WA 98101)
2. Portland Central (456 Oak Ave, Portland, OR 97204)
3. San Francisco Market (789 Market St, San Francisco, CA 94103)
4. Los Angeles Westside (101 Sunset Blvd, Los Angeles, CA 90028)
5. Chicago Loop (202 State St, Chicago, IL 60604)
6. New York Midtown (303 5th Ave, New York, NY 10016)
7. Boston Back Bay (404 Boylston St, Boston, MA 02116)
8. Austin Downtown (505 Congress Ave, Austin, TX 78701)
9. Denver LoDo (606 16th St, Denver, CO 80202)
10. Miami South Beach (707 Ocean Dr, Miami, FL 33139)
11. Atlanta Midtown (808 Peachtree St, Atlanta, GA 30308)
12. Phoenix Downtown (909 Central Ave, Phoenix, AZ 85004)

Answer in the context of Origin Kitchen’s vegetarian, sustainable mission. Avoid suggesting non-vegetarian items.
""",
            },
            {"role": "user", "content": prompt}
        ])
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

    try:
        ai_response = completion.choices[0].message.content
    except (AttributeError, IndexError):
        return JsonResponse({"error": "Unexpected API response structure."}, status=500)

    return JsonResponse({"response": ai_response})
