'''
    Given a file and assume that you can only read the file using a given method read4, implement a method read to read n characters. Your method read may be called multiple times.

    Method read4:

    The API read4 reads 4 consecutive characters from the file, then writes those characters into the buffer array buf.

    The return value is the number of actual characters read.

    Note that read4() has its own file pointer, much like FILE *fp in C.

'''

# class Solution:
#     def __init__(self):
#         self.bp = 0
#         self.read_chars = 0
#         self.buffer = [''] * 4
#
#     def read4(self, buffer):
#         """
#         The API read4 reads 4 consecutive characters from the file,
#         then writes those characters into the buffer array buf.
#         The return value is the number of actual characters read.
#
#         :param buffer:
#         :return:Number of characters that were read.
#         """
#         return buffer
#
#     def read(self, buf, n):
#         """
#         :type buf: Destination buffer (List[str])
#         :type n: Number of characters to read (int)
#         :rtype: The number of actual characters read (int)
#         """
#         tot_chars = 0
#         while tot_chars < n:
#             if self.bp == self.read_chars:
#                 self.bp = 0
#                 self.read_chars = self.read4(self.buffer)
#                 if self.read_chars == 0:
#                     break
#             buf[tot_chars] = self.buffer[self.bp]
#             tot_chars += 1
#             self.bp += 1
#         return tot_chars


class Solution:
    def __init__(self):
        self.q = []

    def read(self, buf, n):
        '''
        buf4 is the destination buffer were the characters are written
        q is a list that is used to store the values that were written with buf4
        n is the number of characters to read
        rtype: i is the number of read characters
        '''
        i = 0
        while i < n:
            if self.q:
                buf[i] = self.q.pop(0)
                i += 1
            else:
                buf4 = [''] * 4
                read_chars = read4(buf4)
                if read_chars == 0:
                    break
                self.q += buf4[:read_chars]
            print(self.q)
        return i

'''
    Time complexity: O(M*N) where M is the number of values in the list and N is the number of times we need to call 
    Space complexity: O(N) 

'''
