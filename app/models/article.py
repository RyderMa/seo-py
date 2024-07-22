from sqlalchemy import Column, ForeignKey, String, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import INTEGER, LONGTEXT, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Article(Base):
    __tablename__ = 'article'
    __table_args__ = {'comment': '文章表'}

    article_id = Column(String(64), primary_key=True,
                        server_default=text("uuid()"), comment='主键id')
    title = Column(String(1024), comment='文章标题')
    desc = Column(Text, comment='文章简介')
    keywords = Column(Text, comment='文章关键字')
    type_level_1 = Column(String(64), comment='文章一级类型')
    type_level_2 = Column(String(64), comment='文章二级类型')
    add_time = Column(TIMESTAMP, nullable=False, server_default=text(
        "current_timestamp()"), comment='添加时间')
    update_time = Column(TIMESTAMP, nullable=False, server_default=text(
        "current_timestamp() ON UPDATE current_timestamp()"), comment='更新时间')
    delete_flag = Column(TINYINT(4), nullable=False,
                         index=True, server_default=text("0"), comment='删除标记')
    status = Column(TINYINT(4), nullable=False, server_default=text(
        "0"), comment='文章状态, 默认0-草稿, 1-待审核, 2-已审核/待发布, 3-已发布, 4-审批驳回')
    publish_time = Column(TIMESTAMP, comment='发布时间')
    source = Column(String(255), comment='文章来源')
    author = Column(String(255), comment='文章作者')
    pv = Column(INTEGER(11), nullable=False,
                server_default=text("0"), comment='访问量')
    uv = Column(INTEGER(11), nullable=False,
                server_default=text("0"), comment='访问用户数')
    tp_user_id = Column(String(64), nullable=False, comment='创建人用户id')
    approve_time = Column(TIMESTAMP, comment='审核时间')
    approve_user_id = Column(String(64), comment='审核人用户id')
    reason = Column(Text, comment='审批驳回原因')
    publish_user_id = Column(String(64), comment='发布人id')
    clue_flag = Column(TINYINT(4), nullable=False,
                       server_default=text("0"), comment='是否线索留资')
    app_id = Column(ForeignKey('app.app_id'), index=True, comment='应用id')
    push_time = Column(TIMESTAMP, comment='文章推送百度时间')
