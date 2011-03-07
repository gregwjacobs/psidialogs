from itertools import count

class AllMixin:
    def multi_choice(self, args):
        r = self.choice(args)
        if r:
            r = [r]
        else:
            r = None
        return r
        
    def text(self, args):
        args = args.copy()
        args.message = args.message + '\n' + args.text 
        args.text = None
        self.message(args)
        
    def choice(self, args):
        args = args.copy()
        lines = [ '[%s] %s' % x  for x in zip(count(), args.choices) ]
        args.message += '\n' + '\n'.join(lines) 
        args.message += '\nSelect:'
##        self.text(args)
        args.default=str(args.default)
        i = self.ask_string(args)
        if not i:
            return None
        i = int(i)
        if i >= 0 and i < len(args.choices):
            return args.choices[i]
        else:
            return None

    def error(self, args):
        self.warning(args)

    def warning(self, args):
        self.message(args)

    def ask_file(self, args):
        return self.ask_string(args)

    def ask_folder(self, args):
        return self.ask_string(args)

#    def button_choice(self, args):
#        result = self.choice(args)
#        return result

    def ask_yes_no(self, args):
        return self.ask_ok_cancel(args)
