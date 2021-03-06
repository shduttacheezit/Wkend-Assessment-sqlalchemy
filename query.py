"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?

# This is a class of a BaseQuery object. 
# Its "type" returns <class 'flask_sqlalchemy.BaseQuery'>. 
# This query needs class or instance methods to return records. 



# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?

# An association table is generally for tables that have a many to many type relationship. 
# It does not contain any meaninful fields the way a middle table does because 
# it only connects the two tables through their primary keys that are also foreign keys.  





# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the brand_id of ``ram``.
q1 = Brand.query.filter_by(brand_id='ram').first()

# Get all models with the name ``Corvette`` and the brand_id ``che``.
q2 = db.session.query(Model).filter(Model.name=='Corvette', Model.brand_id=='che').all()

# Get all models that are older than 1960.
q3 = Model.query.filter(Model.year<1960).all()

# Get all brands that were founded after 1920.
q4 = db.session.query(Brand).filter(Brand.founded>1920).all()

# Get all models with names that begin with ``Cor``.
q5 = Model.query.filter(Model.name.like('%Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = Brand.query.filter((Brand.founded == 1903) & (Brand.discontinued == None)).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = Brand.query.filter((Brand.discontinued != None) | (Brand.founded < 1950)).all()

# Get all models whose brand_id is not ``for``.
q8 = Model.query.filter_by(Model.brand_id!='for').all()



# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    model_info = db.session.query(Model.name, Brand.name, Brand.headquarters).filter(Model.year=='1960').all()

    for model in model_info: 
        print "Model name: %s" % (model[0]), "\nBrand name: %s" % (model[1]), "\nHeadquarted in %s" % (model[2])



def get_brands_summary():
    """Prints out each brand name (once) and all of that brand's models,
    including their year, using only ONE database query."""

    brands_sum = db.session.query(Brand.name, Model.name, Model.year).join(Model).order_by(Brand.name).all()

    summary = []

    for brand_name, model_name, year in brands_sum:
        if brand_name not in summary:
            summary.append(brand_name)
            print "Brand: %s" % (brand_name)
        else: 
            print " Model: %s" % (model_name), "Year: %s" % (year) 

def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    search = Brand.query.filter(Brand.name.match(mystr)).all()

    return search


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    models = Model.query.filter(Model.year>=start_year, Model.year=<end_year).all()

    return models


