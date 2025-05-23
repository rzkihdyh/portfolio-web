from django.shortcuts import render

def index(request):
    # Data untuk template
    context = {
        'name': 'Rizki Hidayatul Laeli',
        'description': "I'm a passionate 4th semester Information Systems student at the Faculty of Computer Science, University of Indonesia. With a strong curiosity in finance, business intelligence, and project management, I'm constantly seeking opportunities to grow, learn, and make real impact.",
        'extended_description': "I thrive in collaborative environments, value critical thinking, and love solving problems through both data and people. Currently open to internship opportunities where I can contribute and grow alongside a dynamic team.",
        
        'social_links': {
            'linkedin': 'https://linkedin.com/in/your-profile',  # Ganti dengan link Anda
            'email': 'mailto:your-email@example.com',  # Ganti dengan email Anda
            'medium': 'https://medium.com/@your-profile'  # Ganti dengan profile Medium Anda
        },
        
        'skills': ['Power BI', 'Django', 'Python', 'Java', 'Figma'],
        
        'interests': [
            'Finance',
            'Business Intelligence & Data Analysis',
            'Project Management'
        ],
        
        'projects': {
            'web': [
                {
                    'name': 'RnD (PKPL)',
                    'description': 'A web-based platform for managing car rentals and allowing users to easily search, book, and rent cars (team)',
                    'url': 'https://kelompok-42-rnd-frontend.pkpl.cs.ui.ac.id/',
                    'type': 'Team Project'
                },
                {
                    'name': 'Sajiwara (PBP)',
                    'description': 'A web-based platform for culinary in Yogyakarta (team)',
                    'url': 'http://theresia-tarianingsih-sajiwaraweb.pbp.cs.ui.ac.id/',
                    'type': 'Team Project'
                }
            ],
            'design': [
                {
                    'name': 'VitaMind',
                    'description': 'A mobile app prototype designed to support GenZ and Millenials mental health',
                    'url': 'https://bit.ly/PrototypeVitaMind',
                    'type': 'Figma Prototype'
                }
            ],
            'business': [
                {
                    'name': 'Parkiran - Business Plan',
                    'description': 'A parking solution business idea developed in a team project',
                    'url': 'https://drive.google.com/drive/folders/1Rc87E7j-nZDA98WFa-cHhnclDZNMn3Y4?usp=sharing',
                    'type': 'Business Plan'
                }
            ],
            'iot': [
                {
                    'name': 'Sahabat Netra',
                    'description': 'An assistive technology prototype to help the visually impaired',
                    'url': 'https://drive.google.com/file/d/1pNUWKtGv9R86CCRdFsf07fmX_NgXAxdB/view?usp=drive_link',
                    'type': 'IoT Prototype'
                }
            ],
            'bi': [
                {
                    'name': 'Business Intelligence Project',
                    'description': 'Advanced data analysis and visualization project',
                    'url': '#',
                    'type': 'Coming Soon'
                }
            ]
        },
        
        'social_projects': [
            'Interkom 1',
            'Interkom 2',
            'JOIN'
        ],
        
        'experiences': {
            'high_school': [
                'Treasurer of Class Batch',
                'Treasurer of MPS (Student Assembly)',
                'ICARE Supervisor',
                'Treasurer of IAIC Roadshow',
                'Member -- Informatics Study Club',
                'Sonic Linguistic -- Associate of Science Competition'
            ],
            'university': [
                'IT Project Manager -- FUKI UI',
                'Vice Manager of Finance -- COMPFEST 17',
                'Treasurer -- SIWAK NG 2024',
                'Finance Associate -- TEDxUniversitasIndonesia',
                'Academic Staff -- BETIS Fasilkom UI',
                'Mentor -- DDP 0 (Intro to Programming, Python)'
            ],
            'organization': [
                'SALAM UI -- Community Division Associate',
                'BEM FASILKOM UI -- Community Service Department Associate',
                'FUKI UI -- Vice Head Business Professional Department'
            ]
        },
        
        'awards': [
            'Top 4 -- National IgnITe Mini Case Challenge',
            'Awardee -- Beasiswa Indonesia Bangkit (LPDP x Kemenag) 2023',
            'Best Graduate Graduated 2023 -- MAN Insan Cendekia Serpong',
            'Most Collaborative Project -- KIHAJAR STEM 2022 (Team)',
            'Awardee -- Ilimac Scholarship'
        ],
        
        'languages': {
            'Indonesian': 'Native',
            'English': 'Professional Working Proficiency',
            'Korean': 'Elementary'
        },
        
        'tools': {
            'languages_frameworks': ['Python', 'Java', 'Django'],
            'design_prototyping': ['Figma'],
            'other_skills': ['Financial management', 'Leadership', 'Project coordination']
        }
    }
    
    return render(request, 'main/index.html', context)