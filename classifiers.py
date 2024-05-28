from main import *

modelLR = LogisticRegression(
    n_jobs=-1,
    max_iter=1000
)

modelKNN = KNeighborsClassifier(
    n_neighbors=3,
    algorithm="ball_tree",
    leaf_size=40,
    weights='distance',
    n_jobs=-1
)

modelRF = RandomForestClassifier(
    n_estimators=1000,
    criterion='log_loss',
    max_depth=40,
    min_samples_split=2,
    min_samples_leaf=4,
    class_weight='balanced_subsample',
    n_jobs=-1,
)

modelDT = DecisionTreeClassifier(
    criterion='log_loss',
    max_depth=60,
    min_samples_split=4,
    min_samples_leaf=6,
    class_weight='balanced',
)
