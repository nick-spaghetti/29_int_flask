from models import db, connect_db, User, Feedback
from app import app

db.drop_all()
db.create_all()

user1 = User.register('user1', 'asdf', 'user1@email.com', 'user1', 'user')
user2 = User.register('user2', 'asdf', 'user2@email.com', 'user2', 'user')
user3 = User.register('user3', 'asdf', 'user3@email.com', 'user3', 'user')
user4 = User.register('user4', 'asdf', 'user4@email.com', 'user4', 'user')
user5 = User.register('user5', 'asdf', 'user5@email.com', 'user5', 'user')

db.session.add(user1)
db.session.add(user2)
db.session.add(user3)
db.session.add(user4)
db.session.add(user5)
db.session.commit()

t1 = Feedback(title='Elit deserunt aute qui', content='Elit deserunt aute qui consectetur enim aliquip reprehenderit laborum nulla non incididunt aute pariatur. Laborum mollit laborum cillum id velit dolore eiusmod excepteur in cillum dolor tempor labore. Proident velit aliqua consequat cillum cupidatat aliquip exercitation aliquip sit fugiat ut. Et sunt magna pariatur esse consequat id ad. Officia nostrud veniam ea eu. Dolore Lorem dolore qui tempor sunt consequat amet mollit commodo in esse incididunt. Elit sit in eiusmod mollit anim anim laboris minim in amet ut.', username='user1')
t2 = Feedback(title='Veniam voluptate ut pariatur et', content='Veniam voluptate ut pariatur et. Laborum exercitation voluptate non mollit. Aliqua commodo deserunt duis id eiusmod ad cillum eiusmod nulla nisi nulla. Do occaecat id est commodo mollit cillum amet incididunt aliqua qui. Elit minim officia cupidatat tempor minim Lorem. Sint ipsum excepteur laboris enim nisi qui occaecat commodo do ipsum laborum. Amet enim esse quis non magna esse..', username='user1')
t3 = Feedback(title='Officia incididunt enim', content='Officia incididunt enim do officia labore non adipisicing tempor. Ipsum consectetur Lorem fugiat nostrud occaecat ut dolor culpa aliquip cupidatat aliqua incididunt aliqua laborum. Deserunt minim dolor enim pariatur ex. Ut tempor officia occaecat aliquip occaecat. Ut irure do velit velit duis esse ut mollit in consectetur ullamco anim culpa. Est quis sint aliquip non duis dolore do id consequat nisi est laborum aliquip laboris..', username='user2')
t4 = Feedback(title='Culpa aute consectetur tempor qui duis',
              content='Culpa aute consectetur tempor qui duis. Cupidatat proident ullamco fugiat id non amet culpa dolor commodo. Qui ad aute pariatur aliquip incididunt eiusmod nostrud duis reprehenderit. Magna dolor esse id incididunt cupidatat. Aliqua tempor ea elit mollit enim ea Lorem eu est incididunt est.', username='user2')
t5 = Feedback(title='Incididunt officia nisi consectetur', content='Incididunt officia nisi consectetur commodo irure. Amet est sint nulla ad enim labore esse voluptate nulla dolore quis. Tempor nostrud Lorem consequat ut non aute proident deserunt. Quis do sunt ad do. Culpa velit adipisicing sit incididunt reprehenderit dolor labore non nostrud. Exercitation exercitation cupidatat esse commodo enim irure eiusmod.', username='user3')
t6 = Feedback(title='Magna ad dolor labore magna',
              content='Magna ad dolor labore magna. Mollit voluptate cillum velit consequat mollit ullamco aliquip commodo. Ullamco qui aliqua occaecat tempor nisi aute. Ut culpa est id ad incididunt excepteur velit dolore labore commodo reprehenderit officia magna eu..', username='user3')
t7 = Feedback(title='Elit deserunt aute qui consectetur enim', content='Elit deserunt aute qui consectetur enim aliquip reprehenderit laborum nulla non incididunt aute pariatur. Laborum mollit laborum cillum id velit dolore eiusmod excepteur in cillum dolor tempor labore. Proident velit aliqua consequat cillum cupidatat aliquip exercitation aliquip sit fugiat ut. Et sunt magna pariatur esse consequat id ad. Officia nostrud veniam ea eu. Dolore Lorem dolore qui tempor sunt consequat amet mollit commodo in esse incididunt. Elit sit in eiusmod mollit anim anim laboris minim in amet ut.', username='user4')
t8 = Feedback(title='Elit minim officia cupidatat', content='Veniam voluptate ut pariatur et. Laborum exercitation voluptate non mollit. Aliqua commodo deserunt duis id eiusmod ad cillum eiusmod nulla nisi nulla. Do occaecat id est commodo mollit cillum amet incididunt aliqua qui. Elit minim officia cupidatat tempor minim Lorem. Sint ipsum excepteur laboris enim nisi qui occaecat commodo do ipsum laborum. Amet enim esse quis non magna esse..', username='user4')
t9 = Feedback(title='Officia incididunt enim do officia', content='Officia incididunt enim do officia labore non adipisicing tempor. Ipsum consectetur Lorem fugiat nostrud occaecat ut dolor culpa aliquip cupidatat aliqua incididunt aliqua laborum. Deserunt minim dolor enim pariatur ex. Ut tempor officia occaecat aliquip occaecat. Ut irure do velit velit duis esse ut mollit in consectetur ullamco anim culpa. Est quis sint aliquip non duis dolore do id consequat nisi est laborum aliquip laboris..', username='user1')
t10 = Feedback(title='Aliqua tempor ea elit mollit',
               content='Culpa aute consectetur tempor qui duis. Cupidatat proident ullamco fugiat id non amet culpa dolor commodo. Qui ad aute pariatur aliquip incididunt eiusmod nostrud duis reprehenderit. Magna dolor esse id incididunt cupidatat. Aliqua tempor ea elit mollit enim ea Lorem eu est incididunt est.', username='user5')
t11 = Feedback(title='Quis do sunt ad do', content='Incididunt officia nisi consectetur commodo irure. Amet est sint nulla ad enim labore esse voluptate nulla dolore quis. Tempor nostrud Lorem consequat ut non aute proident deserunt. Quis do sunt ad do. Culpa velit adipisicing sit incididunt reprehenderit dolor labore non nostrud. Exercitation exercitation cupidatat esse commodo enim irure eiusmod.', username='user5')
t12 = Feedback(title='Ut culpa est id', content='Magna ad dolor labore magna. Mollit voluptate cillum velit consequat mollit ullamco aliquip commodo. Ullamco qui aliqua occaecat tempor nisi aute. Ut culpa est id ad incididunt excepteur velit dolore labore commodo reprehenderit officia magna eu..', username='user1')

db.session.add(t1)
db.session.add(t2)
db.session.add(t3)
db.session.add(t4)
db.session.add(t5)
db.session.add(t6)
db.session.add(t7)
db.session.add(t8)
db.session.add(t9)
db.session.add(t10)
db.session.add(t11)
db.session.add(t12)

db.session.commit()
