class Const:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise AttributeError('Изменение значения атрибута невозможно')
        else:
            super().__setattr__(name, value)
    def __delattr__(self, item):
        raise AttributeError('Удаление атрибута невозможно')

# TEST_5:
work_obj = Const()

work = ['Designer, textile', 'Research scientist (physical sciences)', 'Heritage manager',
        'Civil engineer, contracting', 'Futures trader', 'Psychotherapist', 'Make',
        'English as a foreign language teacher', 'Publishing copy', 'Probation officer', 'Water quality scientist',
        'Magazine features editor', 'Designer, furniture', 'Merchant navy officer', 'Psychiatrist',
        'Biomedical engineer', 'Education officer, community', 'Paediatric nurse', 'Teacher, adult education',
        'Editor, magazine features', 'Scientist, research (medical)', 'Site engineer', 'Wellsite geologist',
        'Journalist, newspaper', 'Psychologist, prison and probation services', 'Therapist, drama', 'Data scientist',
        'Surveyor, hydrographic', 'Animal technologist', 'Brewing technologist', 'Materials engineer', 'Cabin crew',
        'Electronics engineer', 'Contractor', 'Mechanical engineer', 'Tree surgeon', 'Personal assistant',
        'Patent attorney', 'Librarian, academic', 'Haematologist', 'Conservator, furniture', 'Prison officer',
        'Designer, jewellery', 'Surgeon', 'Retail merchandiser', 'Producer, television/film/video', 'Dentist',
        'Primary school teacher', 'Engineer, mining', 'Theatre director', 'Chief of Staff', 'Forest/woodland manager',
        'Oncologist', 'Geoscientist', 'Clinical embryologist', 'Air cabin crew', 'Statistician', 'Administrator',
        'Occupational psychologist', 'General practice doctor', 'Psychotherapist, dance movement',
        'Environmental education officer', 'Librarian, public', 'Editorial assistant', 'Psychiatric nurse',
        'Colour technologist', 'Operational investment banker', 'Armed forces operational officer', 'Immunologist',
        'Arts administrator', 'Web designer', 'Maintenance engineer', 'Energy manager', 'Theme park manager',
        'Medical physicist', 'Lobbyist', 'Medical illustrator', 'Regulatory affairs officer',
        'Research scientist (maths)', 'Printmaker', 'Designer, industrial/product', 'Architectural technologist',
        'Field seismologist', 'Air traffic controller', 'Waste management officer', 'Firefighter',
        'Occupational therapist', 'Community arts worker', 'Commercial art gallery manager',
        'Public relations account executive', 'Historic buildings inspector/conservation officer',
        'Radiation protection practitioner', 'Editor, film/video', 'Database administrator', 'Youth worker',
        'Chemical engineer', 'Tour manager', 'Aid worker', 'Solicitor', 'Chiropodist']

work_obj.job = work[0]
for job in work[1:]:
    try:
        work_obj.job = job
    except AttributeError as e:
        print(e)