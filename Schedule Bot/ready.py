import discord
from discord.ext import tasks, commands
import json
import os


class Ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.dirPath = os.path.dirname(os.path.realpath(__file__))

    @commands.Cog.listener()
    async def on_ready(self):

        print("Online")

        # data = self.dirPath[:-5] + "/data"

        self.bot.userSchedules = {}

    @commands.command()
    async def help(self, ctx, cmdtype=""):
        mbed = discord.Embed(
            title="Schedule Bot",
            description="Schedule bot used for scheduling events",
            color=discord.Colour.green()
        )
        if (cmdtype == "schedule"):
            mbed.add_field(
                name="Schedule",
                value="!schedule Day Hour Minute :arrow_forward: Schedule event on a time",
                inline=True
            )
        elif (cmdtype == "all"):
            mbed.add_field(
                name="All",
                value="!all :arrow_forward: Display all tasks",
                inline=True
            )
        elif (cmdtype == "delete"):
            mbed.add_field(
                name="Delete",
                value="!delete tasknumber :arrow_forward: Delete specified task",
                inline=True
            )
        elif (cmdtype == "move"):
            mbed.add_field(
                name="Move",
                value="!move tasknumber Day Hour Minute :arrow_forward: Move specified task to specified day",
                inline=True
            )
        elif (cmdtype == "setremind"):
            mbed.add_field(
                name="SetRemind",
                value="!setremind number :arrow_forward: Set the amount of minutes that each event will remind you beforehand",
                inline=True
            )
        else:
            mbed.add_field(
                name="Commands",
                value="!help schedule\n!help all\n!help delete\n!help move\n!help setremind",
                inline=True
            )
        await ctx.send(embed=mbed)

    @commands.command()
    async def shutdown(self, ctx):
        await ctx.send("Shutting Down.")
        await self.bot.close()

    @shutdown.error
    async def shutdown_error(self, ctx, error):
        if isinstance(error, (commands.CommandError)):
            await ctx.send(f"{ctx.author.mention} You are not allowed to use owner commands.")


def setup(bot):
    bot.add_cog(Ready(bot))