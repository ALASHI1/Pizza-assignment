# Generated by Django 3.2.4 on 2021-06-20 15:39

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzavault',
            name='toppings',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('pepperoni', 'Pepperoni'), ('mushroom', 'Mushrooms'), ('onions', 'Onions'), ('sausage', 'Sausage'), ('bacon', 'Bacon'), ('extra cheese', 'Extra cheese'), ('black olives', 'Black olives'), ('tomato', 'Tomato'), ('capsicum', 'Capsicum')], default=None, max_length=81),
        ),
    ]
