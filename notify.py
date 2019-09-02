from plyer import notification

class Notify:
    def ping(rate):
        notification.notify(
            title = 'Bitcoin Price Change Notifier',
            message = 'USD: $' + rate,
            app_icon = None, #C:\\icon_32x32.ico
            timeout = 10 #seconds
        )