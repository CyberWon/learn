#coding:utf-8
import yaml
def YamlDeomLoad():
    yaml_str='''127.0.0.1:
      user: root
      password: 123456x
      port: 22
    '''
    yaml_obj=yaml.load(yaml_str)
    print yaml_obj
def YamlDemoDump():
    obj={'127.0.0.1': {'password': '123456x', 'user': 'root', 'port': 22}}
    yaml_str=yaml.dump(obj)
    print yaml_str
if __name__=='__main__':
    print yaml.dump([1,2,3])
    print yaml.dump(('/etc/','/boot'))
    print yaml.dump({'/etc/','/boot'})
    print yaml.dump({'127.0.0.1': {'password': '123456x', 'user': 'root', 'port': 22}})