'''

通过一下几种方式体现：
依赖注入(Dependency Injection): 这是控制反转最常见的实现方式。
通过将对象的依赖项作为参数传递给构造函数或方法,而不是在类内部创建依赖项,可以实现控制反转。这样可以更好地分离关注点,提高代码的可测试性和可维护性。

'''

class EmailSender:
    def send(self, message):
        print(f"Sending email: {message}")

class OrderProcessor:
    def __init__(self, email_sender):
        self.email_sender = email_sender

    def process_order(self, order):
        # 处理订单逻辑
        self.email_sender.send(f"Order {order} processed")

# 使用依赖注入
email_sender = EmailSender()
order_processor = OrderProcessor(email_sender)
order_processor.process_order("ABC123")

'''
钩子(Hooks): 通过定义钩子函数,允许子类或外部代码在特定时间点执行自定义逻辑,从而实现控制反转。这种方式常见于框架或库的设计中。
'''

class MyFramework:
    def run(self):
        self.before_run()
        # 框架主要逻辑
        self.after_run()

    def before_run(self):
        pass

    def after_run(self):
        pass

class MyApp(MyFramework):
    def before_run(self):
        print("Preparing the application")

    def after_run(self):
        print("Cleaning up the application")

app = MyApp()
app.run()


'''
事件/发布-订阅模式: 通过定义事件和事件处理器,实现控制反转。事件的触发者不需要知道具体的事件处理器,而是由事件处理器自行订阅感兴趣的事件。这种模式可以实现松耦合的设计

'''

class EventManager:
    def __init__(self):

        self.subscribers = {} # 定位为字典数据类型

    def subscribe(self, event_type, callback):
        if event_type not in self.subscribers: # 判断订阅字典中是否存在该类型的事件
            self.subscribers[event_type] = []
            '''
             ？ 这里为啥使用append 而不是直接赋值？ 这里使用append方法 ,使得 键值变得可迭代，在publish 方法中，可用for 循环。从而满足多个callback function 的场景
            '''
        self.subscribers[event_type].append(callback)
        #self.subscribers[event_type] = callback

    def publish(self, event_type, *args, **kwargs):
        if event_type in self.subscribers:
            for callback in self.subscribers[event_type]:
                callback(*args, **kwargs)

# 使用事件/发布-订阅模式
event_manager = EventManager()

def on_order_placed(order):
    print(f"Order {order} placed")

# on_order_placed = callback 回调， "order_placed = event_type "
event_manager.subscribe("order_placed", on_order_placed)
event_manager.publish("order_placed", "ABC123")

