import csv
import sys
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    evidence = []
    label = []

    with open(filename, 'r') as file:
        csv_file = csv.reader(file)
        next(csv_file, None)
        for row in csv_file:
            row[0], row[2], row[4], row[11], row[12], row[13], row[14] = int(row[0]), int(row[2]), int(row[4]), int(
                row[11]), int(row[12]), int(row[13]), int(row[14])
            row[1], row[3], row[5], row[6], row[7], row[8], row[9] = float(row[1]), float(row[3]), float(row[5]), float(
                row[6]), float(row[7]), float(row[8]), float(row[9])
            if row[10] == 'Jan':
                row[10] = 0
            elif row[10] == 'Feb':
                row[10] = 1
            elif row[10] == 'Mar':
                row[10] = 2
            elif row[10] == 'Apr':
                row[10] = 3
            elif row[10] == 'May':
                row[10] = 4
            elif row[10] == 'June':
                row[10] = 5
            elif row[10] == 'Jul':
                row[10] = 6
            elif row[10] == 'Aug':
                row[10] = 7
            elif row[10] == 'Sep':
                row[10] = 8
            elif row[10] == 'Oct':
                row[10] = 9
            elif row[10] == 'Nov':
                row[10] = 10
            elif row[10] == 'Dec':
                row[10] = 11

            if row[15] == 'Returning_Visitor':
                row[15] = 1
            else:
                row[15] = 0

            if row[16] == 'TRUE':
                row[16] = 1
            else:
                row[16] = 0

            evidence.append(row[:17])
            if row[17] == 'TRUE':
                label.append(1)
            else:
                label.append(0)
    file.close()

    return (evidence, label)

    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).
    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)
    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    #raise NotImplementedError


def train_model(evidence, labels):


    model=KNeighborsClassifier(n_neighbors=1)

    model.fit(evidence, labels)

    return model

    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    #raise NotImplementedError


def evaluate(labels, predictions):

    positive_labels=labels.count(1)
    negative_labels=labels.count(0)

    true_pos, true_neg=0, 0
    for i in range(len(predictions)):
        if predictions[i]==labels[i]:
            if predictions[i]==1:
                true_pos+=1
            else:
                true_neg+=1

    sensitivity=true_pos/positive_labels
    specificity=true_neg/negative_labels

    return (sensitivity, specificity)
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificty).
    Assume each label is either a 1 (positive) or 0 (negative).
    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.
    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    #raise NotImplementedError


if __name__ == "__main__":
    main()
