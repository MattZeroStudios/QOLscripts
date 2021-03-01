import dbus.proxies


def send_alert(title, message, icon):
    session = dbus.SessionBus()
    obj_proxy = dbus.proxies.ProxyObject(conn=session, bus_name="org.freedesktop.Notifications",
                                         object_path="/org/freedesktop/Notifications")
    proxy = dbus.proxies.Interface(obj_proxy, "org.freedesktop.Notifications")
    method_proxy = proxy.get_dbus_method("Notify")
    method_proxy("qolscript", dbus.UInt32(0), icon, title, message, [], {}, 5)
