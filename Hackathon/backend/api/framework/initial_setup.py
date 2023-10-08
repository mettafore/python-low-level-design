import time    
from framework.schema import User, Role, RoleAttachment, Permission, Resource, LLMModel, Quota, Context
from framework.database import Session, get_session, get_sorted_list_of_tables
from fastapi import Depends
from sqlalchemy import exc
import boto3
from botocore.exceptions import ClientError
import json
from bcrypt import hashpw, gensalt, checkpw
from models.ResourceModel import ResourceType
from models.PermissionModel import ResourceScopes
from sqlalchemy import text

# ...
def register_user(email: str, password: str, is_admin: bool, session: Session=Depends(get_session)):
    user = session.query(User).filter(User.email == email).first()
    if user:
        return False
    password_bytes = hashpw(bytes(password, "utf-8"), gensalt()).decode()
    new_user = User(email=email, password=password_bytes, is_admin=is_admin)
    session.add(new_user)
    session.commit()
    return True

def create_role_attachment(role_id: int, user_id: int, session: Session=Depends(get_session)):
    role = RoleAttachment(role_id=role_id, user_id=user_id)
    session.add(role)
    session.commit()

def create_resource(name: str, resource_type: str, session: Session=Depends(get_session)):
    resource = Resource(name=name, resource_type=resource_type)
    session.add(resource)
    session.commit()
    

def create_permission(role_id: int, resource_id: int, permission: str, session: Session=Depends(get_session)):
    permission_obj = Permission(role_id=role_id, resource_id=resource_id, action=permission)
    session.add(permission_obj)
    session.commit()

def create_quota(model_id: int, user_id: int, assigned_quota: int, session: Session=Depends(get_session)):
    quota = Quota(model_id=model_id, user_id=user_id, assigned_quota=assigned_quota)
    session.add(quota)
    session.commit()

def create_context(resource_id: int, chat_id: int, session: Session=Depends(get_session)):
    context = Context(resource_id=resource_id, chat_id=None)
    session.add(context)
    session.commit()

def delete_all_tables():
    session = get_session()
    tables = get_sorted_list_of_tables()
 
    for table in reversed(tables):
        if str(table)=="alembic_version":
            continue
        try:
            session.execute(table.delete())
            session.execute(text(f"ALTER SEQUENCE \"{table}_id_seq\" RESTART WITH 1"))
            session.commit()
        except exc.SQLAlchemyError as e:
            print(f"Error occurred during Table: {table} truncate operation; ERROR: {str(e)}")
            


def initial_setup():
    session = get_session()

    role1_flag = create_role(name='superuser', description='Superuser Role', session=session)
    role2_flag = create_role(name='general', description='General Role', session=session)
    user_id, password = get_superuser_credentials()
    suser_flag = register_user(email=user_id, password=password, is_admin=True, session=session)
    session.close()
    session = get_session()
    user = session.query(User).filter(User.email == user_id).first()
    # wait for 2 seconds
    time.sleep(2)
    if role1_flag and role2_flag and suser_flag:
        create_role_attachment(role_id=1, user_id=1, session=session)
        create_role_attachment(role_id=2, user_id=1, session=session)
        # Creating Resources
        create_resource(name='DataScience', resource_type=ResourceType.FILE_REPO.value, session=session)
        create_resource(name='DataScience', resource_type=ResourceType.TABLE_REPO.value, session=session)
        create_resource(name='Operations', resource_type=ResourceType.FILE_REPO.value, session=session)
        create_resource(name='Operations', resource_type=ResourceType.TABLE_REPO.value, session=session)
        create_resource(name='Legal', resource_type=ResourceType.FILE_REPO.value, session=session)
        create_resource(name='Legal', resource_type=ResourceType.TABLE_REPO.value, session=session)        
        # Creating Permission
        create_permission(role_id=1, resource_id=1, permission=ResourceScopes.FileRepo.CreateFiles.value, session=session)
        create_permission(role_id=1, resource_id=1, permission=ResourceScopes.FileRepo.DeleteFiles.value, session=session)
        create_permission(role_id=1, resource_id=1, permission=ResourceScopes.FileRepo.ReadFiles.value, session=session)
        create_permission(role_id=1, resource_id=2, permission=ResourceScopes.TableRepo.CreateTables.value, session=session)
        create_permission(role_id=1, resource_id=2, permission=ResourceScopes.TableRepo.DeleteTables.value, session=session)
        create_permission(role_id=1, resource_id=2, permission=ResourceScopes.TableRepo.ReadTables.value, session=session)
        create_permission(role_id=1, resource_id=3, permission=ResourceScopes.FileRepo.CreateFiles.value, session=session)
        create_permission(role_id=1, resource_id=3, permission=ResourceScopes.FileRepo.DeleteFiles.value, session=session)
        create_permission(role_id=1, resource_id=3, permission=ResourceScopes.FileRepo.ReadFiles.value, session=session)
        create_permission(role_id=1, resource_id=4, permission=ResourceScopes.TableRepo.CreateTables.value, session=session)
        create_permission(role_id=1, resource_id=4, permission=ResourceScopes.TableRepo.DeleteTables.value, session=session)
        create_permission(role_id=1, resource_id=4, permission=ResourceScopes.TableRepo.ReadTables.value, session=session)
        create_permission(role_id=1, resource_id=5, permission=ResourceScopes.FileRepo.CreateFiles.value, session=session)
        create_permission(role_id=1, resource_id=5, permission=ResourceScopes.FileRepo.DeleteFiles.value, session=session)
        create_permission(role_id=1, resource_id=5, permission=ResourceScopes.FileRepo.ReadFiles.value, session=session)
        create_permission(role_id=1, resource_id=6, permission=ResourceScopes.TableRepo.CreateTables.value, session=session)
        create_permission(role_id=1, resource_id=6, permission=ResourceScopes.TableRepo.DeleteTables.value, session=session)
        create_permission(role_id=1, resource_id=6, permission=ResourceScopes.TableRepo.ReadTables.value, session=session)

        create_permission(role_id=2, resource_id=1, permission=ResourceScopes.FileRepo.ReadFiles.value, session=session)
        create_permission(role_id=2, resource_id=2, permission=ResourceScopes.TableRepo.ReadTables.value, session=session)
        create_permission(role_id=2, resource_id=3, permission=ResourceScopes.FileRepo.ReadFiles.value, session=session)
        create_permission(role_id=2, resource_id=4, permission=ResourceScopes.TableRepo.ReadTables.value, session=session)
        create_permission(role_id=2, resource_id=5, permission=ResourceScopes.FileRepo.ReadFiles.value, session=session)
        create_permission(role_id=2, resource_id=6, permission=ResourceScopes.TableRepo.ReadTables.value, session=session)
        # Creating Model
        create_model(name='gpt-3.5-turbo', description='GPT 3.5 Model', is_active=True, session=session)
        create_model(name='gpt-4', description='GPT 4.0 Model', is_active=False, session=session)
        # Creating Quota
        create_quota(model_id=1, user_id=1, assigned_quota=10000, session=session)
        create_quota(model_id=2, user_id=1, assigned_quota=10000, session=session)
        # Creating Context
        create_context(resource_id=1, chat_id=None, session=session)
        create_context(resource_id=2, chat_id=None, session=session)
        create_context(resource_id=3, chat_id=None, session=session)
        create_context(resource_id=4, chat_id=None, session=session)
        create_context(resource_id=5, chat_id=None, session=session)
        create_context(resource_id=6, chat_id=None, session=session)

    session.close()

    
    
    