from app import db, Message

# all_messages = Message.query.all()
# print(all_messages)
# # all_messages[0].name
#
# # message_1 = Message.query.get(1)
# # print(message_1)  #repr result
# # print(message_1.message)  #per obj atributa
#
# message_antanas = Message.query.filter_by(name='Antanas').all()
# print(message_antanas)
#
# # UPDATE
#
# antanas = Message.query.get(2)
# antanas.email = 'geras.antanas@gmail.com'
# print(db.session.dirty)
# db.session.commit()
# print(all_messages)
#
# #DELETE
#
# jonas = Message.query.get(1)
# db.session.delete(jonas)
# db.session.commit()
# print(all_messages)

all_items = Message.query.all()
for item in all_items:
    print(item)

