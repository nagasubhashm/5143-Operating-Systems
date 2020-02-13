#include <omp.h>
#include <cmath>
#include <iostream>

using namespace std;

/**
 * @FunctionName: Queue
 * @Description:
 *     Implementation of a char queue
 */
class Queue {
 private:
  //////////////////////////////////////////////////////

  int ArraySize;
  int *Q;
  int Front;
  int Rear;
  int NumItems;

 public:
  //////////////////////////////////////////////////////

  /**
   * @FunctionName: Queue
   * @Description:
   *     Class constructor
   * @Params:
   *    int insize - initial queue size
   * @Returns:
   *    void
   */
  Queue(int insize) {
    ArraySize = insize;
    Q = new int[ArraySize];
    Front = Rear = NumItems = 0;
  }

  /**
   * @FunctionName: push
   * @Description:
   *     Adds a int to the queue
   * @Params:
   *    char c - int to add
   * @Returns:
   *    void
   */
  void Push(int c) {
    if (Full()) {
      cout << "Queue Full!" << endl;
      return;
    }
#pragma omp critical(push)
    {
      cout<<"p1";
      Q[Rear] = c;
      cout<<"p2";
      Rear = (Rear + 1) % ArraySize;
      cout<<"p3";
      NumItems++;
      cout<<"p4\n";
    }
    return;
  }

  /**
   * @FunctionName: pop
   * @Description:
   *     Returns a int from the top of the queue
   * @Params:
   *    None
   * @Returns:
   *    void
   */
  int Pop() {
    if (Empty()) {
      cout << "Queue Empty!" << endl;
      return false;
    }
    int Temp;
#pragma omp critical(pop)
    {
      cout<<"o1";
      Temp = Q[Front];
      cout<<"o2";
      Front = (Front + 1) % ArraySize;
      cout<<"o3";
      NumItems--;
      cout<<"o4\n";
    }
    return Temp;
  }

  /**
   * @FunctionName: printQueue
   * @Description:
   *     Prints queue to stdout for debugging purposes
   * @Params:
   *    None
   * @Returns:
   *    void
   */
  void PrintQueue() {
    cout << "Queue:";
    for (int i = Front, j = 0; j < NumItems; j++, i = (i + 1) % ArraySize) {
      cout << Q[i] << " ";
    }
    cout << endl;
  }

  /**
   * @FunctionName: empty
   * @Description:
   *     Checks to see if queue is empty.
   * @Params:
   *    None
   * @Returns:
   *    bool - true if empty / false otherwise
   */
  bool Empty() { return (NumItems == 0); }

  /**
   * @FunctionName: full
   * @Description:
   *     Checks if queue is full
   * @Params:
   *    None
   * @Returns:
   *    bool - true if full / false otherwise
   */
  bool Full() { return (NumItems == ArraySize); }

  int Size(){
      return NumItems;
  }
};

int main(int argc, char *argv[]) {
  int th_id, nthreads;
  Queue Q(10000);

#pragma omp parallel private(th_id)
  {
    th_id = omp_get_thread_num();
    //#pragma omp critical
    cout << "Hello World from thread " << th_id << endl;
    //#pragma omp critical(loop) // LOL :)
    #pragma omp for
    for(int i=0;i<100;i++){
        Q.Push(th_id);
        cout<<"size: "<<Q.Size()<<endl;
    }

#pragma omp barrier  //<----------- master waits until all threads finish before
                     //printing
    if (th_id == 0) {
      nthreads = omp_get_num_threads();
      //#pragma omp critical
      cout << "There are  " << nthreads << " threads" << endl;

      Q.PrintQueue();
    }
  }

}  // main