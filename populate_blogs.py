import os
import sys
import django
from django.utils import timezone
from datetime import datetime
import pytz  # Import pytz for timezone handling

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simplygreen.settings')

# Add the project directory to the Python path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

# Initialize Django
django.setup()

from website.models import Blog
from django.db import transaction

def populate_blogs():
    # Blog data
    blogs_data = [
        {
            'title': 'Farm to Table: Why It Matters',
            'author': 'Emma Green',
            'date_posted': datetime(2025, 5, 1, tzinfo=pytz.UTC),
            'preview': 'Learn how Origin Kitchen sources local produce to create fresh, sustainable vegetarian dishes while supporting regional farmers and reducing our carbon footprint.',
            'content': (
                '# Introduction\n'
                'At Origin Kitchen, our farm-to-table philosophy is at the heart of everything we do. By sourcing ingredients directly from local farms, we ensure every dish is fresh, flavorful, and sustainable. But what does farm-to-table really mean, and why is it so important?\n\n'
                '# Supporting Local Farmers\n'
                'Partnering with regional farmers allows us to serve the freshest produce while strengthening our community. For example, our heirloom tomatoes come from Sunny Acres Farm, just 20 miles away. By buying directly, we help small farms thrive and preserve traditional farming practices. This direct relationship also means we can request specific varieties, like purple carrots or microgreens, to elevate our dishes.\n\n'
                '# Reducing Environmental Impact\n'
                'Farm-to-table isn’t just about taste—it’s about the planet. Local sourcing reduces transportation emissions, as our ingredients travel miles, not continents. We also prioritize organic and regenerative farming methods that enrich the soil and sequester carbon. Our commitment to sustainability means every bite you take supports a healthier ecosystem.\n\n'
                '# Flavor You Can Taste\n'
                'Freshly harvested produce bursts with flavor that mass-produced alternatives can’t match. Our chefs design menus around what’s in season, ensuring peak ripeness and nutrition. From crisp summer salads to hearty winter root vegetable stews, our farm-to-table approach delivers vibrant, unforgettable dishes.\n\n'
                '# Conclusion\n'
                'Farm-to-table is more than a trend—it’s a movement that connects us to our food, our farmers, and our planet. At Origin Kitchen, we’re proud to lead the way, one delicious plate at a time. Visit us to taste the difference local makes!'
            ),
            'image': 'blog_images/farm_to_table.jpg',
        },
        {
            'title': 'Meet Our Chef: The Heart of Origin Kitchen',
            'author': 'Liam Carter',
            'date_posted': datetime(2025, 5, 3, tzinfo=pytz.UTC),
            'preview': 'Get to know Chef Maria Alvarez, whose passion for vegetarian cuisine and innovative recipes shape Origin Kitchen’s unforgettable menu.',
            'content': (
                '# Introduction\n'
                'Behind every great restaurant is a visionary chef, and at Origin Kitchen, that’s Chef Maria Alvarez. With a career spanning two decades, Maria’s love for vegetarian cuisine has transformed our menu into a celebration of flavor and sustainability.\n\n'
                '# A Journey to Vegetarian Excellence\n'
                'Maria’s culinary journey began in her grandmother’s kitchen, where she learned to transform simple vegetables into vibrant dishes. After training at Le Cordon Bleu, she worked in Michelin-starred restaurants before embracing vegetarian cuisine. “Vegetables are endlessly versatile,” Maria says. “They inspire me to create dishes that surprise and delight.”\n\n'
                '# Crafting Signature Dishes\n'
                'Maria’s signature creations, like our Butternut Squash Ravioli and Thai Green Curry, showcase her ability to balance bold flavors with fresh ingredients. She spends mornings visiting local farms to select produce, ensuring every dish reflects the season’s best. Her innovative use of herbs and spices, like smoked paprika in our Veggie Tacos, has earned rave reviews.\n\n'
                '# A Vision for the Future\n'
                'Beyond the kitchen, Maria is committed to mentoring young chefs and promoting sustainable cooking. She hosts workshops at Origin Kitchen, teaching guests how to make plant-based meals at home. Her goal? To make vegetarian cuisine accessible and exciting for everyone.\n\n'
                '# Conclusion\n'
                'Chef Maria Alvarez is the soul of Origin Kitchen, blending creativity, passion, and sustainability in every dish. Join us to experience her culinary magic and see why she’s a leader in vegetarian dining.'
            ),
            'image': 'blog_images/farm_to_table.jpg',
        },
        {
            'title': 'Seasonal Menu Highlights: Spring 2025',
            'author': 'Sophie Nguyen',
            'date_posted': datetime(2025, 5, 5, tzinfo=pytz.UTC),
            'preview': 'Explore Origin Kitchen’s spring 2025 menu, featuring fresh asparagus, peas, and radishes in dishes that celebrate the season’s bounty.',
            'content': (
                '# Introduction\n'
                'Spring is a time of renewal, and at Origin Kitchen, our spring 2025 menu reflects the vibrant flavors of the season. From tender asparagus to sweet peas, our chefs have crafted dishes that highlight the freshest produce available.\n\n'
                '# Starters That Shine\n'
                'Our new Asparagus Tart, made with flaky puff pastry and vegan ricotta, is a must-try appetizer. The crisp asparagus spears are paired with a lemon zest drizzle, creating a light yet indulgent start to your meal. Another favorite is the Pea and Mint Soup, a velvety blend that captures spring’s essence in every spoonful.\n\n'
                '# Main Courses to Savor\n'
                'For entrees, our Spring Vegetable Risotto is a standout, featuring arborio rice cooked with peas, radishes, and a touch of white wine. The dish is finished with vegan parmesan for a creamy, satisfying texture. We’ve also introduced a Grilled Artichoke Plate, served with a herb-infused aioli that’s perfect for sharing.\n\n'
                '# Sweet Endings\n'
                'Don’t miss our Rhubarb and Strawberry Crumble for dessert. The tart rhubarb and sweet strawberries are baked under a crunchy oat topping, served with a scoop of vegan vanilla ice cream. It’s the perfect way to end a spring meal.\n\n'
                '# Conclusion\n'
                'Our spring 2025 menu is a love letter to seasonal produce, crafted with care to delight your palate. Visit Origin Kitchen to experience these limited-time dishes before summer arrives!'
            ),
            'image': 'blog_images/farm_to_table.jpg',
        },
        {
            'title': 'Sustainability in Action: Our Eco-Friendly Kitchen',
            'author': 'Emma Green',
            'date_posted': datetime(2025, 5, 7, tzinfo=pytz.UTC),
            'preview': 'From composting to zero-waste practices, see how Origin Kitchen minimizes its environmental impact while serving delicious vegetarian meals.',
            'content': (
                '# Introduction\n'
                'Sustainability is more than a buzzword at Origin Kitchen—it’s a way of life. Our commitment to eco-friendly practices ensures that every dish we serve supports a healthier planet, from the kitchen to your plate.\n\n'
                '# Composting and Waste Reduction\n'
                'We compost all food scraps, turning vegetable peels and leftovers into nutrient-rich soil for local farms. Our zero-waste initiative has reduced landfill contributions by 80% since 2023. We also use biodegradable packaging for takeout orders, eliminating single-use plastics.\n\n'
                '# Energy and Water Efficiency\n'
                'Our kitchen is equipped with energy-efficient appliances, and we’ve installed low-flow faucets to conserve water. Solar panels power 30% of our restaurant, and we’re working toward 100% renewable energy by 2030. These efforts lower our carbon footprint without compromising quality.\n\n'
                '# Sustainable Sourcing\n'
                'We prioritize local, organic ingredients to reduce transportation emissions and support regenerative farming. Our menu is designed to minimize waste, with dishes like our Root-to-Leaf Soup that use every part of the vegetable. This approach ensures nothing goes to waste.\n\n'
                '# Conclusion\n'
                'At Origin Kitchen, sustainability is woven into everything we do. By dining with us, you’re supporting a greener future. Join us to enjoy delicious food that’s good for you and the planet!'
            ),
            'image': 'blog_images/farm_to_table.jpg',
        },
        {
            'title': 'Community Spotlights: Our Farmers and Partners',
            'author': 'Liam Carter',
            'date_posted': datetime(2025, 5, 9, tzinfo=pytz.UTC),
            'preview': 'Meet the farmers and artisans who bring Origin Kitchen’s farm-to-table vision to life, from organic greens to handcrafted vegan cheeses.',
            'content': (
                '# Introduction\n'
                'Origin Kitchen’s mission is built on community. Our farmers, artisans, and partners are the backbone of our farm-to-table philosophy, providing the ingredients and inspiration for our menu.\n\n'
                '# Sunny Acres Farm\n'
                'Sunny Acres, a family-owned farm, supplies our organic greens and root vegetables. Farmer Jane Patel’s dedication to regenerative agriculture ensures our salads are fresh and sustainable. Her heirloom carrots are the star of our Roasted Vegetable Bowl, adding vibrant color and flavor.\n\n'
                '# Artisan Vegan Cheese Co.\n'
                'Our vegan cheeses come from Artisan Vegan Cheese Co., a local producer known for its creamy cashew-based creations. Their smoked cheddar elevates our Plant-Based Nachos, offering a rich, dairy-free alternative that even non-vegans love. Owner Miguel Torres shares our passion for sustainability.\n\n'
                '# Building Stronger Communities\n'
                'Beyond sourcing, we collaborate with partners on community initiatives, like donating surplus produce to food banks and hosting farm tours for local schools. These efforts strengthen our ties and educate the next generation about sustainable food systems.\n\n'
                '# Conclusion\n'
                'Our farmers and partners make Origin Kitchen special. By dining with us, you’re supporting a network of passionate people dedicated to quality and sustainability. Visit us to taste their hard work!'
            ),
            'image': 'blog_images/farm_to_table.jpg',
        },
        {
            'title': 'The Art of Vegan Desserts: Sweet Without Sacrifice',
            'author': 'Sophie Nguyen',
            'date_posted': datetime(2025, 5, 10, tzinfo=pytz.UTC),
            'preview': 'Discover how Origin Kitchen creates decadent vegan desserts, like our Chocolate Lava Cake, using plant-based ingredients that rival traditional sweets.',
            'content': (
                '# Introduction\n'
                'Vegan desserts at Origin Kitchen prove you don’t need dairy to indulge. From our Chocolate Lava Cake to Mango Sticky Rice, our sweets are crafted to satisfy every craving while staying true to our plant-based values.\n\n'
                '# Innovative Ingredients\n'
                'Our pastry chefs use coconut milk, cashew cream, and aquafaba to replicate the richness of traditional desserts. For example, our Vegan Chocolate Mousse is made with silken tofu and dark chocolate, creating a velvety texture without cream. These ingredients are both sustainable and delicious.\n\n'
                '# Balancing Flavor and Health\n'
                'We prioritize natural sweeteners like maple syrup and dates to keep our desserts lighter. Our Carrot Cake with Cashew Frosting uses almond flour for a gluten-free option, packed with nutrients. Each dessert is designed to feel indulgent yet guilt-free.\n\n'
                '# Guest Favorites\n'
                'Our Berry Crumble, with its mix of seasonal berries and oat topping, is a crowd-pleaser. Guests also rave about our Pistachio Baklava, which layers flaky phyllo with a vegan honey syrup. These desserts showcase the versatility of plant-based baking.\n\n'
                '# Conclusion\n'
                'Vegan desserts at Origin Kitchen are proof that sustainability and indulgence go hand in hand. Stop by to try our sweet creations and see how delicious plant-based can be!'
            ),
            'image': 'blog_images/farm_to_table.jpg',
        },
        {
            'title': 'Cooking with Herbs: Elevating Vegetarian Dishes',
            'author': 'Emma Green',
            'date_posted': datetime(2025, 5, 11, tzinfo=pytz.UTC),
            'preview': 'Learn how Origin Kitchen uses fresh herbs like basil, cilantro, and thyme to transform simple vegetarian dishes into flavor-packed meals.',
            'content': (
                '# Introduction\n'
                'Herbs are the secret weapon in Origin Kitchen’s kitchen. From fragrant basil to earthy thyme, fresh herbs elevate our vegetarian dishes, adding depth and complexity to every bite.\n\n'
                '# The Power of Fresh Herbs\n'
                'Unlike dried herbs, fresh ones offer vibrant flavors and aromas. Our Caprese Skewers rely on basil’s peppery sweetness to complement tomatoes and mozzarella. Similarly, cilantro brightens our Veggie Tacos, balancing the smoky spices with a fresh, citrusy note.\n\n'
                '# Growing Our Own\n'
                'We grow herbs in our on-site garden, ensuring a steady supply of organic basil, rosemary, and mint. This allows our chefs to experiment, like infusing thyme into our Mushroom Stroganoff sauce. Guests can even tour the garden during our monthly open house events.\n\n'
                '# Tips for Home Cooks\n'
                'Want to cook like us? Chop herbs just before using to preserve their flavor, and add delicate ones like parsley at the end of cooking. For inspiration, try our recipe for Herb-Infused Quinoa Salad, available on our website.\n\n'
                '# Conclusion\n'
                'Herbs are small but mighty, transforming vegetarian cuisine with minimal effort. Visit Origin Kitchen to taste how we use them, or join our cooking classes to master herbs at home!'
            ),
            'image': 'blog_images/farm_to_table.jpg',
        },
        {
            'title': 'The Benefits of Vegetarian Diets: Health and Beyond',
            'author': 'Liam Carter',
            'date_posted': datetime(2025, 5, 12, tzinfo=pytz.UTC),
            'preview': 'Explore the health, environmental, and ethical benefits of vegetarian diets, and see how Origin Kitchen makes plant-based eating delicious and accessible.',
            'content': (
                '# Introduction\n'
                'Vegetarian diets are gaining popularity, and for good reason. At Origin Kitchen, we believe plant-based eating is not only delicious but also transformative for your health and the planet.\n\n'
                '# Health Advantages\n'
                'Studies show vegetarian diets reduce the risk of heart disease, diabetes, and certain cancers. Our Mediterranean Quinoa Bowl, packed with fiber-rich quinoa and antioxidants, supports heart health. Plant-based meals are also lower in saturated fats, helping you feel energized and balanced.\n\n'
                '# Environmental Impact\n'
                'Choosing vegetarian reduces your carbon footprint. Producing plant-based foods emits far less greenhouse gas than meat. By dining at Origin Kitchen, you’re supporting sustainable agriculture, as our ingredients come from eco-friendly farms.\n\n'
                '# Ethical Considerations\n'
                'Vegetarianism aligns with compassionate values, minimizing harm to animals. Our vegan dishes, like the BBQ Jackfruit Bowl, prove you can enjoy bold flavors without animal products. We’re proud to offer a menu that’s kind to all living beings.\n\n'
                '# Conclusion\n'
                'A vegetarian diet offers benefits for your body, the environment, and your conscience. At Origin Kitchen, we make it easy to embrace plant-based eating with dishes that delight. Try us today!'
            ),
            'image': 'blog_images/farm_to_table.jpg',
        },
        {
            'title': 'Behind the Scenes: How Our Kitchen Runs',
            'author': 'Sophie Nguyen',
            'date_posted': datetime(2025, 5, 13, tzinfo=pytz.UTC),
            'preview': 'Take a peek inside Origin Kitchen’s bustling kitchen, where teamwork, precision, and passion create your favorite vegetarian dishes.',
            'content': (
                '# Introduction\n'
                'Ever wondered what happens behind the scenes at Origin Kitchen? Our kitchen is a hive of activity, where chefs, prep cooks, and staff work together to bring you exceptional vegetarian meals.\n\n'
                '# A Day in the Kitchen\n'
                'Each day starts with deliveries from local farms, followed by prep work like chopping vegetables and soaking grains. Our chefs collaborate on daily specials, ensuring every dish meets our high standards. By lunchtime, the kitchen is in full swing, with stations dedicated to grilling, sautéing, and plating.\n\n'
                '# Teamwork Makes the Dream Work\n'
                'Our team is a family, from our head chef to our dishwashers. Regular training sessions keep everyone sharp, and we encourage creativity, like when a prep cook suggested our popular Tempura Green Beans. This collaborative spirit ensures consistency and innovation.\n\n'
                '# Technology and Efficiency\n'
                'We use smart kitchen tools, like inventory tracking software, to minimize waste. Our energy-efficient ovens and induction burners reduce energy use, aligning with our sustainability goals. These systems help us serve you faster without sacrificing quality.\n\n'
                '# Conclusion\n'
                'Our kitchen is the heart of Origin Kitchen, where passion and precision come together. Book a kitchen tour to see us in action, or simply enjoy the results at your table!'
            ),
            'image': 'blog_images/farm_to_table.jpg',
        },
        {
            'title': 'Pairing Drinks with Vegetarian Dishes: A Perfect Match',
            'author': 'Emma Green',
            'date_posted': datetime(2025, 5, 15, tzinfo=pytz.UTC),
            'preview': 'Learn how to pair Origin Kitchen’s vegetarian dishes with our drinks, from kombucha to turmeric lattes, for a harmonious dining experience.',
            'content': (
                '# Introduction\n'
                'A great drink can elevate a meal, and at Origin Kitchen, our beverage menu is designed to complement our vegetarian dishes. From crisp juices to warm lattes, we’ve got the perfect pairing for every plate.\n\n'
                '# Refreshing Pairings\n'
                'Our Cold-Pressed Green Juice, with its blend of kale and apple, is a refreshing match for our Mediterranean Quinoa Bowl. The juice’s bright acidity cuts through the tahini dressing, creating a balanced bite. Similarly, our Hibiscus Iced Tea pairs beautifully with spicy dishes like the Jalapeno Burger.\n\n'
                '# Warm and Cozy Options\n'
                'For heartier entrees like our Lentil & Veggie Shepherd’s Pie, try our Golden Turmeric Latte. Its warm, spicy notes complement the dish’s savory flavors. Our Vegan Hot Chocolate is a decadent pairing for desserts like the Carrot Cake, enhancing its nutty sweetness.\n\n'
                '# Experimenting with Kombucha\n'
                'Our rotating kombucha flavors add a fizzy, probiotic boost to lighter dishes. The ginger kombucha enhances our Thai Peanut Noodle Salad, echoing its tangy profile. Ask your server for the day’s flavor to find your ideal match.\n\n'
                '# Conclusion\n'
                'Pairing drinks with vegetarian dishes is an art, and Origin Kitchen makes it easy. Explore our beverage menu to find your perfect combination, and elevate your next meal with us!'
            ),
            'image': 'blog_images/farm_to_table.jpg',
        },
    ]

    try:
        with transaction.atomic():
            # Delete all existing blog posts
            deleted_count = Blog.objects.all().delete()[1]
            print(f"Successfully deleted {deleted_count} existing blog posts.")

            # Create new blog posts
            created_count = 0
            for blog_data in blogs_data:
                Blog.objects.create(
                    title=blog_data['title'],
                    content=blog_data['content'],
                    preview=blog_data['preview'],
                    image=blog_data['image'],
                    date_posted=blog_data['date_posted'],
                )
                created_count += 1

            print(f"Successfully created {created_count} new blog posts.")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    populate_blogs()