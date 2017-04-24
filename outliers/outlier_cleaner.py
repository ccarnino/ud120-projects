#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here
    import numpy

    training_set_count = len(predictions)

    # Calculate the error for each prediction
    errors = numpy.zeros(training_set_count)
    for index in range(training_set_count):
        errors[index] = abs(predictions[index] - net_worths[index])

    errors = errors.tolist()

    # Create working tuple
    working_data = []
    for indexItem in range(training_set_count):
        working_data.append(tuple([ages[indexItem][0], net_worths[indexItem][0], errors[indexItem]]))

    # Calculate how many entries have to keept (90% of the dataset)
    numberItemsKeep = int(training_set_count * 0.9)

    # Loop over all the working data
    for indexItem in range(numberItemsKeep):
        # Find the item with the smallest error
        errorsArray = numpy.array(errors)
        indexLowestError = numpy.where(errorsArray == min(errorsArray))[0][0]
        # Append the item to the final cleaned data
        clean_value = working_data[indexLowestError]
        cleaned_data.append(clean_value)
        # Remove the item with the lowest error from the working data and from the error array
        # working_data.remove(indexLowestError)
        # errors.remove(indexLowestError)
        del working_data[indexLowestError]
        del errors[indexLowestError]

    return cleaned_data
