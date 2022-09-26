import discord
from discord.ext import tasks, commands
import random
import json
import os
import time
import classes

class Good(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.dirPath = os.path.dirname(os.path.realpath(__file__))

    def getText(self, task):
        msg = str(task.curTime.day) + " " + str(task.curTime.hours) + " " + str(
            task.curTime.minutes) + " " + task.name + "\n"
        return msg

    @commands.command(name="schedule")
    async def sched(self, ctx, name, da, hr, mi):
        # curTime = time.mktime(time.time())
        # handle invalid input
        try:
            da = int(da)
            hr = int(hr)
            mi = int(mi)
        except:
            await ctx.send("Invalid parameters.")
            return
        # main code

        temp = classes.Task(name, da, hr, mi)

        userid = str(ctx.author.id)

        if userid not in self.bot.userSchedules:
            self.bot.userSchedules[userid] = classes.Schedule()

        self.bot.userSchedules[userid].addTask(temp)

        await ctx.send(f"{ctx.author.mention} Task succesfully added.")

    @commands.command(name="delete")
    async def delete(self, ctx, index):
        try:
            index = int(index)
        except:
            await ctx.send("Invalid parameters.")
            return

        userid = str(ctx.author.id)

        if userid not in self.bot.userSchedules:
            self.bot.userSchedules[userid] = classes.Schedule()

        if (self.bot.userSchedules[userid].deleteTask(index)):
            await ctx.send(f"{ctx.author.mention} Task succesfully deleted.")
        else:
            await ctx.send(f"{ctx.author.mention} No such task exists.")

    @commands.command(name="all")
    async def showSched(self, ctx):

        # replace with something nicer later

        userid = str(ctx.author.id)
        if userid not in self.bot.userSchedules:
            self.bot.userSchedules[userid] = classes.Schedule()

        if (len(self.bot.userSchedules[userid].taskList) == 0):
            await ctx.send(f"{ctx.author.mention} No pending tasks.")
        else:
            msg = ""
            cnt = 0
            for i in self.bot.userSchedules[userid].taskList:
                cnt += 1;
                msg += "(" + str(cnt) + ") " + self.getText(i)

            mbed = discord.Embed(
                title=str(ctx.author)[:-5] + "'s Tasks",
                description=msg,
                colour=discord.Colour.green()
            )
            await ctx.send(embed=mbed)


def setup(bot):
    bot.add_cog(Good(bot))