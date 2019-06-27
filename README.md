# JianZhiOffer
剑指offer的题目

## 题目列表
题3：数组中的重复数字：
+ 3.1：[[牛客]](https://www.nowcoder.com/practice/623a5ac0ea5b4e5f95552655361ae0a8?tpId=13&tqId=11203&tPage=3&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking) 解法：哈希 或者 考虑数字范围为0~n-1的重排数组
+ 3.2：[[leetcode]](https://leetcode-cn.com/problems/find-the-duplicate-number/) 
+ 解法：二分 或者 快慢指针

题4：二维数组中的查找 [[牛客]](https://www.nowcoder.com/practice/abc3fe2ce8e146608e868a70efebf62e?tpId=13&tqId=11154&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking) 
+ 解法：从右上角元素开始比较

题5：替换空格 [[牛客]](https://www.nowcoder.com/practice/4060ac7e3e404ad1a894ef3e17650423?tpId=13&tqId=11155&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking) 
+ 解法：主要考察C语言字符串的问题

题6：从尾到头打印链表 [[牛客]](https://www.nowcoder.com/practice/d0267f7f55b3412ba93bd35cfa8e8035?tpId=13&tqId=11156&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)  
+ 解法：栈 或者 递归

题7：重建二叉树 [[牛客]](https://www.nowcoder.com/practice/8a19cbe657394eeaac2f6ea9b0f6fcf6?tpId=13&tqId=11157&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
+ 解法：递归。每次先找根结点，然后递归左子结点和右子结点。

题8：二叉树的下一个结点 [[牛客]](https://www.nowcoder.com/practice/9023a0c988684a53960365b889ceaf5e?tpId=13&tqId=11210&tPage=3&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
+ 解法1：分3类讨论。有右子树；是父节点的左节点；父节点的右节点则回溯
+ 解法2：先求根结点，然后把中序求出来

题9：用两个栈实现队列 [[牛客]](https://www.nowcoder.com/practice/54275ddae22f475981afa2244dd448c6?tpId=13&tqId=11158&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking) 
+ 解法：栈1用来push，栈2为空则把栈1导进来再pop，栈2不为空直接pop

题10：斐波那契数列 [[leetcode]](https://leetcode-cn.com/problems/fibonacci-number/)
+ 解法：递归 或者 循环（速度远超递归）
+ 类似的题目：[[爬楼梯/跳台阶]](https://leetcode-cn.com/problems/climbing-stairs/) 动态规划的思想，发现递推方程为斐波那契数列

题13：机器人的运动范围 [[牛客]](https://www.nowcoder.com/practice/6e5207314b5241fb83f2329e89fdecc8?tpId=13&tqId=11219&tPage=4&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
+ 解法：回溯

题14：剪绳子
+ 解法：动态规划，dp[i]代表长度为i的绳子的最大乘积，如dp[4]=max(dp[1]*dp[3],dp[2]*dp[2])，注意刚开始的3个是例外。

题18：删除链表的节点 [[leetcode]](https://leetcode-cn.com/problems/delete-node-in-a-linked-list/)
+ 解法：将下一个结点的内容复制到当前结点，然后删除下一个结点即可

题42：连续子数组的最大和 [[leetcode]](https://leetcode-cn.com/problems/maximum-subarray/)
+ 解法1：找规律，O(N)
+ 解法2：动态规划，O(N)，dp[i]表示以第i个元素结尾的子数组的最大和

题45：把数组排成最小的数 [[牛客]](https://www.nowcoder.com/practice/8fecd3f8ba334add803bf2a06af1b993?tpId=13&tqId=11185&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking)
+ 解法：排序+重写字符串比较大小