from ansiblelint import AnsibleLintRule
import os

class ModuleYumWithoutWithItems(AnsibleLintRule):
    id = 'E403'
    shortdesc = "Yum shouldn't has with_items argument  "
    description = (
        '[DEPRECATION WARNING]: Invoking "yum" only once while using a loop via '
        'squash_actions is deprecated. Instead ofusing a loop to supply multiple '
        'items and specifying `name: "{{ item }}"`, please use '
        '`name: [\'binutils\', \'make\', \'ruby\', \'git\']` and remove the loop. '
        'This feature will be removed in version 2.11. '
    )
    tags = ['module']

    def matchtask(self, file, task):
        if task['action']['__ansible_module__'] != 'yum':
            return False

        if 'with_items' in task:
            return True
        return False
