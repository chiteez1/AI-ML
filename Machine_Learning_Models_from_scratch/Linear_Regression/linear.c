#include <stdio.h>
#include <math.h>

// This is a re-implementation of my linear regression model in C. I did this for fun.

// function to sum an arr
double sum(double *ptr, int len)
{
    double sm = 0;
    for (int i = 0; i < len; i++)
    {
        sm += ptr[i];
    }
    return sm;
}

// function to calculate mean of arr
double mean(double *ptr, int len)
{
    return sum(ptr, len) / len;
}

// function to calculate loss
double loss(double *y_pred, double *y_true, int len)
{
    double avg_loss = 0.0, diff;
    for (int i = 0; i < len; i++)
    {
        diff = *(y_true + i) - *(y_pred + i);
        avg_loss += (diff * diff);
    }
    return avg_loss / len;
}

// function to calculate gradients
void gradients(double *x, double *y_pred, double *y_true, int n, double *dw, double *db)
{
    // calculate error
    double err[n];
    for (int i = 0; i < n; i++)
    {
        err[i] = *(y_pred + i) - *(y_true + i);
    }

    // calculate gradients
    // for bias
    *db = 2.0 * mean(err, n);

    // for weight
    for (int i = 0; i < n; i++)
    {
        // err * x
        err[i] *= x[i];
    }
    *dw = 2.0 * mean(err, n);
}

// linear regression function
void linear_reg(double *features, double *labels, double *w, double *b, int len)
{
    // starting values
    *w = 0.1;
    *b = 0.2;
    int patience = 100, epochs = 10000, wait = 0;
    double pd[len], dw, db, low_l = INFINITY, curr_l, lr = 0.01;

    for (int i = 0; i < epochs; i++)
    {
        // prediction
        for (int j = 0; j < len; j++)
        {
            pd[j] = ((*w) * features[j]) + (*b);
        }

        // calculate loss
        curr_l = loss(pd, labels, len);
        printf("Current loss: %.15lf\n", curr_l);

        // check if current loss is lower than lowest loss
        if (curr_l < low_l)
        {
            wait = 0;
            low_l = curr_l;
        }

        // if not, increase wait by 1;
        else
        {
            wait++;
        }

        // stops the loop if loss keeps increasing for given number of iterations
        if (wait >= patience)
        {
            break;
        }

        // calculate derivatives for weight and bias
        gradients(features, pd, labels, len, &dw, &db);

        // update weigth and bias
        *w -= (lr * dw);
        *b -= (lr * db);
    }
    printf("Lowest loss: %.15lf\n", low_l);
}

int main()
{
    // test the model
    double x[] = {1, 2, 3, 4, 5}, y[5], w = 0.1, b = 0.2;
    for (int i = 0; i < 5; i++)
    {
        y[i] = (2 * x[i]) + 3;
    }
    linear_reg(x, y, &w, &b, 5);
    printf("Weight: %lf\n", w);
    printf("Bias: %lf\n", b);
    return 0;
}
