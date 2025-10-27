from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import selectinload

engine = create_engine('postgresql://postgres:viking676@localhost:5432/LW2Povarnina')
Session = sessionmaker(bind=engine)
session = Session()

from models import User, Address, Product, Order

# Создание 5 пользователей с адресами
for i in range(1, 6):
    user = User(name=f'User {i}')
    address = Address(email=f'user{i}@example.com', user=user)
    session.add(user)
    session.add(address)

session.commit()
session.close()


users = session.query(User).options(selectinload(User.addresses)).all()

for user in users:
    print(f"User: {user.name}")
    for address in user.addresses:
        print(f"  Address: {address.email}")


# Добавление 5 продуктов
for i in range(1, 6):
    product = Product(name=f'Product {i}', price=100 * i)
    session.add(product)

# Добавление 5 заказов
users = session.query(User).all()
addresses = session.query(Address).all()
products = session.query(Product).all()

for i in range(5):
    order = Order(
        user_id=users[i].id,
        address_id=addresses[i].id,
        product_id=products[i].id
    )
    session.add(order)

session.commit()
session.close()
