"""
Hard-coded CV data for the experience page.
Both English and Chinese versions from Li Xiaochuan's CV.
"""

EXPERIENCE = {
    'en': [
        {
            'company': 'BOSCH — XC Division',
            'title': 'Perception Algorithm Expert',
            'period': 'Aug 2025 – Present',
            'bullets': [
                'Designed and implemented a federated learning training framework for an EU OEM overseas production program, enabling cross-region joint optimization under strict data-localization compliance (GDPR / CN law) — raw data never leaves its region.',
                'Delivered float and QAT federated training for the EU dynamic perception model; EU visual perception KPIs improved at every release milestone with zero regression on the China-side baseline.',
                'Explored knowledge distillation as an annotation-free alternative to reduce EU labeled-data dependency; student model reached teacher-level accuracy in internal evaluation.',
                'Contributed to the EU OEM static lane model mass-production SOP: profiled training-set distribution, designed scenario-weighted re-sampling, and enforced pre-training data quality gates.',
                'Co-established a JIRA-driven road-test closed-loop: sprint-level corner-case re-sampling, similarity-based hard-sample mining, and structured data-acquisition requirements per release cycle.',
            ],
        },
        {
            'company': 'WeRide — L3 Mass Production Perception',
            'title': 'Algorithm Engineer',
            'period': 'Apr 2024 – Jul 2025',
            'bullets': [
                'Ground-lock detection (long-tail, ~2% of data): bootstrapped training with synthetic positives and iteratively reduced false positives via negative mining — final model: 76% precision / 81% recall.',
                'Parking E2E RL optimization: built RL environment with bicycle-kinematics constraints, designed reward function, migrated training to Stable Baselines3 — park-in rate improved from 81% to 86%.',
                'Free Space model: extended ground-truth coverage to 120 m via spatio-temporal joint labeling, scaled model query size, and preserved raw segmentation output to avoid ray-casting information loss.',
                'Free Space daily iteration: owned JIRA case analysis and scene-level benchmark construction; mined data for hard scenarios (intersections, U-turns); cut labeling pipeline time by 235% via pcl load_from_memory and time-window caching.',
            ],
        },
        {
            'company': 'Li Auto — Smart Driving',
            'title': 'Algorithm Engineer',
            'period': 'Jul 2022 – Mar 2024',
            'bullets': [
                'Built auto-labeling pipeline for construction-zone scenes, achieving >98% accuracy at 10M+ data scale — eliminating manual annotation cost for the majority of training data.',
                'Built and iterated the scene-understanding baseline model: ultra-long-range (120–200 m) construction warning accuracy >80%; deployed on-vehicle with post-processing suppression that eliminated all known false-trigger cases.',
                'Built automated hard-case mining pipeline for traffic-light perception: 5k clips/day at >70% accuracy; implemented resolution logic and ensured T+1 turnaround on short-term operational issues.',
                'Built inference/evaluation/visualization pipeline for the static BEV-Occupancy joint model, enabling independent on-vehicle accuracy validation.',
                'On-vehicle deployment: cut TensorRT inference latency from 75 ms to 44 ms (7.3 Hz → 12.5 Hz); built vehicle-side alignment debugging toolchain.',
                'RDMA task-parallel training: designed architecture and led module development — 300% throughput improvement over serial baseline.',
                'DALI/cv-CUDA decode pipeline: 2000% and 150% speed-up within <1% numerical error. Mixed-precision training module resolved VRAM fluctuation, significantly reducing peak memory footprint.',
            ],
        },
    ],
    'zh': [
        {
            'company': '博世 — XC 感知算法部门',
            'title': '感知算法专家',
            'period': '2025年8月 — 至今',
            'bullets': [
                '针对EU OEM出海量产项目的数据合规要求（GDPR / 国内数据法规），设计并实现联邦学习训练框架，通过高频权重交换实现跨区域联合优化，全程无需共享原始数据。',
                '在EU动态感知模型上实现float/QAT联邦训练，每个版本里程碑EU视觉感知指标持续提升，国内基线指标无回退。',
                '探索知识蒸馏作为减少EU标注数据依赖的备选方案；student模型在EU指标内测中达到与teacher模型相当的精度，验证了无标注训练方向的可行性。',
                '参与EU OEM静态车道线模型量产SOP建设：统计训练集数据分布，设计场景加权重采样策略，建立训练前数据质量门控。',
                '与团队共同建立基于JIRA的路测闭环迭代流程：sprint级corner case重采样、相似度挖掘扩展失败样本、按版本周期提出结构化数据采集需求。',
            ],
        },
        {
            'company': '文远知行 — L3量产项目感知组',
            'title': '算法工程师',
            'period': '2024年4月 — 2025年7月',
            'bullets': [
                '地锁离线检测（长尾场景，含锁数据约2%）：采用生成方式获取正样本启动训练，通过负样本挖掘迭代减少误检，最终模型达到76%准确率 / 81%召回率。',
                '泊车两段式端到端优化：搭建基于自行车运动学模型的RL基础交互环境，设计Reward函数并基于Stable Baselines3完成训练代码迁移，泊入率从81%提升至86%。',
                'Free Space视觉感知模型优化：采用时空联合标注将真值范围扩充至120m；调整模型规模与query size；保留分割原始输出，避免打射线过程导致信息丢失。',
                'Free Space任务日常迭代：负责路测JIRA case分析汇总，搭建分场景benchmark数据集；针对路口/掉头等困难场景挖掘数据；通过pcl库load_from_memory函数、时间窗cache等方法提升标注效率235%。',
            ],
        },
        {
            'company': '理想汽车 — 智能驾驶',
            'title': '算法工程师',
            'period': '2022年7月 — 2024年3月',
            'bullets': [
                '搭建施工场景自动标注流水线，在千万级数据规模上达到98%以上准确率，大幅降低人工标注成本。',
                '负责场景理解基线模型搭建、迭代与优化：高速超远距离（120～200m）施工场景预警准确率超过80%；完成车端部署并添加后处理抑制策略，对已知场景实现误触发清零。',
                '搭建红绿灯难样本自动挖掘流水线，达成每日5k clip难样本数据交付，准确率超过70%；负责部分红绿灯解题逻辑实现，确保短线问题T+1解决。',
                '搭建联合模型推理/评测/可视化链路，支撑团队独立完成车端精度验证与版本迭代。',
                '负责车端部署优化：TensorRT推理耗时从75ms优化至44ms（7.3Hz→12.5Hz）保证模型上车；开发车端对齐调试工具，完成车端与本地模型精度对齐。',
                '负责基于RDMA的任务并行训练架构设计与模块开发，整体提速300%。',
                '基于DALI/cv-cuda的数据解码/预处理模块开发，实现1%误差以内2000%和150%的速度提升；负责多任务训练框架下混合精度训练模块开发，显著降低峰值显存占用。',
            ],
        },
    ],
}

INTERNSHIP = {
    'en': {
        'company': 'Huawei Technologies — Optical Product Line',
        'title': 'AI Engineer Intern',
        'period': 'Jun 2021 – Dec 2021',
        'bullets': [
            'Implemented dual-lamp fitting algorithm for intelligent vehicle-light solution; completed hardware demo.',
            'Proposed automated freeform-surface calibration method (improved speed and accuracy over prior methods) — awarded SPDT TA Star.',
        ],
    },
    'zh': {
        'company': '华为技术有限公司 — 光产品线',
        'title': 'AI工程师（实习）',
        'period': '2021年6月 — 2021年12月',
        'bullets': [
            '参与智能车载光解决方案攻关，实现双车灯拟合关键算法并配合硬件完成演示。',
            '提出针对自由曲面投影显示的自动化标定方法，提高标定速度和准确率，获得SPDT TA Star嘉奖。',
        ],
    },
}

EDUCATION = {
    'en': [
        {
            'school': 'Beihang University',
            'degree': 'Master · System Engineering',
            'period': 'Sep 2019 – Jun 2022',
            'gpa': 'GPA: 3.65 / 4',
            'notes': 'First Prize Academic Scholarship 2020',
            'courses': 'AI Principles & Applications, Information System Integration, Computer Graphics',
        },
        {
            'school': 'École Centrale de Lille',
            'degree': "Master (Dual Degree) · General Engineer",
            'period': 'Aug 2018 – Jul 2020',
            'gpa': 'GPA: 3.65 / 4',
            'notes': '',
            'courses': 'Operations Research, Advanced Algorithms, OOP, Signal Processing',
        },
        {
            'school': 'Beihang University',
            'degree': 'Bachelor · Information and Computational Science',
            'period': 'Sep 2015 – Jun 2019',
            'gpa': 'GPA: 3.50 / 4',
            'notes': 'National Encouragement Scholarship · CVPR ug2+ Challenge (10/200)',
            'courses': '',
        },
    ],
    'zh': [
        {
            'school': '北京航空航天大学',
            'degree': '硕士研究生 · 系统工程',
            'period': '2019年9月 — 2022年6月',
            'gpa': 'GPA: 3.65/4',
            'notes': '2020年学业奖学金一等奖',
            'courses': '人工智能原理与应用、信息系统集成技术、计算机图形学',
        },
        {
            'school': '法国里尔中央理工学院',
            'degree': '硕士研究生（双学位） · 通用工程师',
            'period': '2018年8月 — 2020年7月',
            'gpa': 'GPA: 3.65/4',
            'notes': '',
            'courses': '运筹学、算法进阶、面向对象编程、信号处理',
        },
        {
            'school': '北京航空航天大学',
            'degree': '本科 · 信息与计算科学',
            'period': '2015年9月 — 2019年6月',
            'gpa': 'GPA: 3.50/4',
            'notes': '国家励志奖学金 · CVPR ug2+挑战赛（10/200）',
            'courses': '',
        },
    ],
}

SKILLS = {
    'en': {
        'Languages': 'CET-6 566/710 · TOEIC 935/990 · French TCF B2',
        'Perception': 'BEV Perception, Object Detection, Semantic Segmentation, Lane Detection, Free Space, Scene Understanding',
        'ML / Training': 'Federated Learning, Knowledge Distillation, Mixed-Precision Training, Distributed Training, Reinforcement Learning (SB3)',
        'Deployment': 'TensorRT, CUDA, DALI, cv-CUDA, on-vehicle debugging',
        'Programming': 'Python (proficient), C/C++ (proficient), Java (working knowledge)',
    },
    'zh': {
        '语言': '大学英语六级 566/710 · TOEIC 935/990 · 法语TCF B2',
        '感知算法': 'BEV感知、目标检测、语义分割、车道线检测、Free Space、场景理解',
        'ML / 训练': '联邦学习、知识蒸馏、混合精度训练、分布式训练、强化学习（SB3）',
        '部署工具': 'TensorRT、CUDA、DALI、cv-CUDA、车端调试',
        '编程语言': '熟练：Python、C/C++；掌握：Java',
    },
}

PROFILE = {
    'en': (
        'Perception Algorithm Engineer with 3+ years in autonomous driving, '
        'specializing in camera-based visual perception and production model delivery. '
        'Currently at BOSCH XC Division as Expert, contributing to the EU OEM overseas '
        'production program through federated learning and data-compliant training pipelines. '
        'Prior experience in L3 mass production perception at WeRide (BEV free space, object detection) '
        'and City NOA at Li Auto (scene understanding, traffic lights, joint BEV-Occupancy model). '
        'Proven track record of closing the full loop from data engineering to on-vehicle deployment.'
    ),
    'zh': (
        '3年以上自动驾驶视觉感知算法经验，专注于基于纯视觉的BEV感知与量产模型交付。'
        '现就职于博世XC感知算法部门（感知算法专家），参与EU OEM出海量产项目，'
        '负责联邦学习合规训练框架与模型迭代交付。此前在文远知行（L3量产BEV感知/目标检测）'
        '和理想汽车（城市NOA场景理解/红绿灯/联合BEV-Occupancy模型）'
        '积累了完整的数据工程到车端部署全链路经验。'
    ),
}
