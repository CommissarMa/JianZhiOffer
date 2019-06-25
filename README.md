# JianZhiOffer
剑指offer的题目

## 题目列表
题8：二叉树的下一个结点 [[牛客]](https://www.nowcoder.com/practice/9023a0c988684a53960365b889ceaf5e?tpId=13&tqId=11210&tPage=3&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
+ 解法1：分3类讨论。有右子树；是父节点的左节点；父节点的右节点则回溯
+ 解法2：先求根结点，然后把中序求出来

题42：连续子数组的最大和 [[leetcode]](https://leetcode-cn.com/problems/maximum-subarray/)
+ 解法1：找规律，O(N)
+ 解法2：动态规划，O(N)，dp[i]表示以第i个元素结尾的子数组的最大和

题45：把数组排成最小的数 [[牛客]](https://www.nowcoder.com/practice/8fecd3f8ba334add803bf2a06af1b993?tpId=13&tqId=11185&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking)
+ 解法：排序+重写字符串比较大小