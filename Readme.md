> When I complete my current work, I will organize the code as soon as possible.

## Installation
- I use pytorch1.1.0, cuda9.0/10.0, and mmcv0.4.3.



#####  Test with a single GPU

```shell
python tools/test.py ${CONFIG_FILE} ${CHECKPOINT_FILE} [--out ${RESULT_FILE}] [--eval ${EVAL_METRICS}] [--show]
```

#####  Test with multiple GPUs

```shell
./tools/dist_test.sh ${CONFIG_FILE} ${CHECKPOINT_FILE} ${GPU_NUM} [--out ${RESULT_FILE}] [--eval ${EVAL_METRICS}]
```



More instructions will come soon！
