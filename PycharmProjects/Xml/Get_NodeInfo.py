from xml.dom import minidom
dom=minidom.parse('Class_info.xml')
root=dom.documentElement
print(root.nodeName)
print(root.nodeValue)
print(root.nodeType) #元素节点1 属性节点2
