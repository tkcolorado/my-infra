from ansible.module_utils.basic import *
def main():
    module = AnsibleModule(argument_spec=dict(
        num=dict(type='int', required=True),
        touch=dict(type='bool', default=False)))

    result = dict(
        changed=False,
        sum = 0
    )

    num = module.params['num']
    touch = module.params.get('touch')

    for i in range(1, num+1):
        result['sum'] += i

    if touch:
        touch_file = '/tmp/test.txt'
        import subprocess
        subprocess.run(['touch', touch_file])
        result['touch'] = touch_file
        result['changed'] = True

    module.exit_json(**result)
    
if __name__ == '__main__':
    main()