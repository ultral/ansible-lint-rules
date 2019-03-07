from ansiblelint import AnsibleLintRule
import os

class ModulePipWithoutWithItems(AnsibleLintRule):
    id = 'E404'
    shortdesc = "Pip shouldn't has with_items argument "
    description = (
        '[DEPRECATION WARNING]: Invoking "pip" only once while using a loop via '
        'squash_actions is deprecated. Instead of using a loop to supply multiple '
        'items and specifying `name: "{{ item }}"`, please use '
        '`name: \'{{ ansible_pip_modules }}\'` and remove the loop. '
        'This feature will be removed in version 2.11. '
    )
    tags = ['module']

    def matchtask(self, file, task):
        if task['action']['__ansible_module__'] != 'pip':
            return False

        if 'with_items' in task:
            return True
        return False
