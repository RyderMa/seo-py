from sqlalchemy import Column, ForeignKey, String, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import INTEGER, LONGTEXT, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
metadata = Base.metadata


class App(Base):
    __tablename__ = 'app'
    __table_args__ = {'comment': '应用表'}

    app_id = Column(String(64), primary_key=True,
                    server_default=text("uuid()"), comment='主键id')
    app_name = Column(String(255), comment='应用名称')
    slogan = Column(String(1024), comment='标语')
    domain_name = Column(String(1024), comment='域名')
    first_api = Column(String(64), comment='一级路由')
    seo_api = Column(String(1024), comment='百度SEO推送API')
    add_time = Column(TIMESTAMP, nullable=False, server_default=text(
        "current_timestamp()"), comment='创建时间')
    update_time = Column(TIMESTAMP, nullable=False, server_default=text(
        "current_timestamp() ON UPDATE current_timestamp()"), comment='更新时间')
    tp_user_id = Column(String(64), comment='创建人id')
    delete_flag = Column(TINYINT(4), nullable=False,
                         server_default=text("0"), comment='删除标记')
    keywords = Column(Text, comment='应用首页关键字')
    description = Column(Text, comment='应用首页描述')


class AppTemplate(Base):
    __tablename__ = 'app_template'
    __table_args__ = {'comment': '应用模版配置数据表'}

    app_template_id = Column(
        String(255), primary_key=True, server_default=text("uuid()"), comment='主键id')
    app_id = Column(ForeignKey('app.app_id'), nullable=False,
                    index=True, comment='应用id')
    template_id = Column(ForeignKey('template.template_id'),
                         nullable=False, index=True, comment='模版id')
    config = Column(Text, comment='配置数据')
    delete_flag = Column(TINYINT(4), nullable=False,
                         server_default=text("0"), comment='删除标记')
    tp_user_id = Column(String(64), comment='创建人id')
    add_time = Column(TIMESTAMP, nullable=False, server_default=text(
        "current_timestamp()"), comment='创建时间')
    updat_time = Column(TIMESTAMP, nullable=False, server_default=text(
        "current_timestamp() ON UPDATE current_timestamp()"), comment='更新时间')

    app = relationship('App')
    template = relationship('Template')


class DictArticleType(Base):
    __tablename__ = 'dict_article_type'
    __table_args__ = {'comment': '文章分类字典表'}

    dict_article_type_id = Column(
        VARCHAR(64), primary_key=True, server_default=text("uuid()"), comment='主键id')
    level = Column(TINYINT(4), nullable=False,
                   server_default=text("1"), comment='分类级别, 1-一级, 2-二级')
    name = Column(String(255), nullable=False, comment='分类名称')
    delete_flag = Column(TINYINT(4), nullable=False,
                         server_default=text("0"), comment='删除标记')
    img_url = Column(String(255), comment='分类默认图片地址')
    app_id = Column(ForeignKey('app.app_id'), index=True, comment='应用id')
    sort = Column(INTEGER(11), nullable=False,
                  server_default=text("0"), comment='排序字段')
    key = Column(String(255), comment='分类关键字(首页路由使用)')

    app = relationship('App')


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


class ArticleDetail(Base):
    __tablename__ = 'article_detail'
    __table_args__ = {'comment': '文章详情表'}

    article_detail_id = Column(
        String(64), primary_key=True, server_default=text("uuid()"), comment='主键id')
    article_id = Column(ForeignKey('article.article_id'),
                        nullable=False, index=True, comment='文章id')
    comment = Column(LONGTEXT, comment='文章内容')
    delete_flag = Column(TINYINT(4), nullable=False,
                         server_default=text("0"), comment='删除标记')

    article = relationship('Article')


class ArticleImg(Base):
    __tablename__ = 'article_img'
    __table_args__ = {'comment': '文章配图表'}

    article_img_id = Column(String(64), primary_key=True, comment='主键id')
    article_id = Column(ForeignKey('article.article_id'),
                        nullable=False, index=True, comment='文章id')
    img_url = Column(String(1024), nullable=False, comment='图片url')

    article = relationship('Article')
